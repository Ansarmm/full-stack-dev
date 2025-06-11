from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

app = FastAPI()

users = []
current_id = 0

class User(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    access_key: int



@app.post('/users', response_model = User)
async def create_user(new_user: UserCreate):
    global current_id

    for user in users:
        if user.email == new_user.email:
            raise HTTPException(status_code=400, detail="This email is already registered")
        
    current_id += 1

    if new_user.access_key == 125:
        user_role = "Admin"
    else:
        user_role = "User"

    add_user = User(id=current_id, name=new_user.name, role=user_role, email=new_user.email)
    users.append(add_user)
    return add_user


@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int):

    for user in users:
        if user.id == user_id:
            return user
        
    raise HTTPException(status_code=404, detail="User not found")

@app.get('/users')
async def get_users():
    return users

@app.delete('/users/{user_id}')
async def delete_user(user_id: int):

    for index,user in enumerate(users):
        if user.id == user_id:
            deleted = users.pop(index)
            return {
                "message": f"User with id {user_id} deleted",
                "deleted user": deleted
            }
        
    raise HTTPException(status_code=404, detail="User not found")

@app.put('/users/{user_id}', response_model=User)
async def update_user(user_id: int, updated_user: UserCreate):

    for user in users:
        if user.email == updated_user.email and user.id != user_id:
            raise HTTPException(status_code=400, detail="This email is already used by another user")
        
    if updated_user.access_key == 125:
        user_role = "Admin"
    else:
        user_role = "User"

    for index,user in enumerate(users):
        if user.id == user_id:
            users[index] = User(id=user.id, name=updated_user.name, role=user_role, email=updated_user.email)
            return users[index]
        
    raise HTTPException(status_code=404, detail="User not found")