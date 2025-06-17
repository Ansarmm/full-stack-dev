from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import bcrypt
from jose import jwt
from datetime import datetime, timedelta
from uuid import uuid4
from pydantic import BaseModel


# Конфигурация для JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10
REFRESH_TOKEN_EXPIRE_MINUTES = 30


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


app = FastAPI()
users = []
access_tokens = []
active_refresh_tokens = {}


def create_access_token(data: dict):
    # Добавляем дату истечения токена
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})  # Поле "exp" указывает, когда токен истечет

    # Генерируем токен
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def create_refresh_token(email: str):
    token_id = str(uuid4())  # Генерируем уникальный идентификатор
    expire = datetime.utcnow() + timedelta(minutes=REFRESH_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": email, "id": token_id, "exp": expire}
    refresh_token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    # Сохраняем токен как активный
    active_refresh_tokens[token_id] = {"email": email, "expires_at": expire}
    return refresh_token


def verify_access_token(token: str):
    try:
        if not access_tokens or token != access_tokens[-1]:
            raise HTTPException(status_code=401, detail="Token is no longer valid")

        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Возвращаем данные токена, если он валиден

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")
 

def check_user_role(token_data: dict, required_role: str):
    user_role = token_data.get("role")
    if user_role != required_role:
        raise HTTPException(
            status_code=403,
            detail=f"Access denied: requires {required_role} role"
        )


@app.post("/auth/register")
def register_user(
    name: str,
    email: str,
    password: str,
    role: str = "user"
):
    if any(u["email"] == email for u in users):
        return {"error": "Email already exists"}

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "password": hashed_password,
        "role": role
    }

    users.append(new_user)
    return {"message": "User registered successfully"}


@app.post("/auth/login")
def login_user(form_data: OAuth2PasswordRequestForm = Depends()):
    email = form_data.username
    password = form_data.password

    user = next((u for u in users if u["email"] == email), None)
    if not user or not bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        return {"error": "Invalid email or password"}

    # Удаляем все активные Refresh Tokens для этого пользователя
    tokens_to_revoke = [key for key, value in active_refresh_tokens.items() if value["email"] == email]
    for token_id in tokens_to_revoke:
        del active_refresh_tokens[token_id]

    access_token = create_access_token({"sub": user["email"], "role": user["role"], "name": user["name"]})
    refresh_token = create_refresh_token(user["email"])

    access_tokens.append(access_token)
    return {
        "access_token": access_token,
        "refresh_token": refresh_token
    }


@app.get("/protected")
def protected_route(access_token: str = Depends(oauth2_scheme)):
    # Проверяем токен
    user_data = verify_access_token(access_token)
    return {"message": f"Welcome, your role is {user_data['role']}",
            "Your access token": access_token,

        }


@app.get("/me")
def get_current_user(token: str = Depends(oauth2_scheme)):
    # Проверяем токен
    user_data = verify_access_token(token)
    return {
        "email": user_data["sub"],
        "name": user_data["name"],
        "role": user_data["role"]
    }

    
    
@app.get("/admin")
def admin_route(token: str = Depends(oauth2_scheme)):
    user_data = verify_access_token(token)
    check_user_role(user_data, "admin")
    return {"message": "Welcome, Admin! You have full access."}


@app.get("/user-resource")
def user_resource(token: str = Depends(oauth2_scheme)):
    user_data = verify_access_token(token)
    check_user_role(user_data, "user")
    return {"message": f"Welcome, {user_data['name']}! This resource is for users only."}



@app.post("/auth/refresh")
def refresh_access_token(refresh_token: str):
    try:
        # Проверяем валидность Refresh Token
        payload = jwt.decode(refresh_token, SECRET_KEY, algorithms=[ALGORITHM])
        token_id = payload.get("id")
        email = payload.get("sub")

        # Проверяем, что токен активен
        if token_id not in active_refresh_tokens:
            raise HTTPException(status_code=401, detail="Refresh token is not active")
        
        del active_refresh_tokens[token_id]

        user = next((u for u in users if u["email"] == email), None)

        if not user:
            raise HTTPException(status_code=404, detail="User not found")
        # Генерируем новый Access Token
        new_access_token = create_access_token({"sub": user["email"], "role": user["role"], "name": user["name"]})
        new_refresh_token = create_refresh_token(email)

        access_tokens.append(new_access_token)

        return {
            "new access_token": new_access_token,
            "new refresh token": new_refresh_token       
        }

    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Refresh token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@app.post("/auth/logout")
def logout_user(token: str = Depends(oauth2_scheme)):
    # Проверяем токен
    payload = verify_access_token(token)
    email = payload.get("sub")

    # Удалить все Access Tokens
    access_tokens.clear()

    # Удаляем все активные Refresh Tokens пользователя
    tokens_to_revoke = [key for key, value in active_refresh_tokens.items() if value["email"] == email]
    for token_id in tokens_to_revoke:
        del active_refresh_tokens[token_id]

    return {"message": "Successfully logged out"}



current_id = 0
tasks = []


class Task(BaseModel):
    id: int
    name: str
    status: bool

class TaskCreate(BaseModel):
    name: str
    status: bool


@app.post('/tasks', response_model = Task)
def create_task(task: TaskCreate, token: str = Depends(oauth2_scheme)):
    user = verify_access_token(token)
    global current_id
    current_id += 1

    new_task = {
        "id": current_id,
        "name": task.name,
        "status": task.status,
        "owner": user["sub"]
    }
    tasks.append(new_task)
    return Task(id=new_task["id"], name=new_task["name"], status=new_task["status"])


@app.get("/tasks")
def list_tasks(token: str = Depends(oauth2_scheme)):
    user = verify_access_token(token)
    user_tasks = [t for t in tasks if t["owner"] == user["sub"]]
    return {"tasks": user_tasks}


@app.get("/tasks/{task_id}")
def get_task(task_id: int, token: str = Depends(oauth2_scheme)):
    user = verify_access_token(token)
    task = next((t for t in tasks if t["id"] == task_id and t["owner"] == user["sub"]), None)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"task": task}


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskCreate, token: str = Depends(oauth2_scheme)):
    user = verify_access_token(token)
    existing_task = next((t for t in tasks if t["id"] == task_id and t["owner"] == user["sub"]), None)
    if not existing_task:
        raise HTTPException(status_code=404, detail="Project not found")

    existing_task.update({
        "name": task.name,
        "status": task.status
    })
    return {"message": "Task updated", "task": existing_task}

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, token: str = Depends(oauth2_scheme)):
    user = verify_access_token(token)
    global tasks
    tasks = [t for t in tasks if not (t["id"] == task_id and t["owner"] == user["sub"])]
    return {"message": "Task deleted"}