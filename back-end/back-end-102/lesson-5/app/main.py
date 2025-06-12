from fastapi import FastAPI, Body
import bcrypt

app = FastAPI()
users = []

@app.post("/auth/register")
def register_user(
    name: str = Body(...),
    email: str = Body(...),
    password: str = Body(...),
    role: str = Body("user")
):
    if any(u["email"] == email for u in users):
        return {"error": "Email already exists"}

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "password": hashed_password,
        "role": role,
    }
    users.append(new_user)
    return {"message": "User registered successfully"}

@app.post("/auth/login")
def login_user(
    email: str = Body(...),
    password: str = Body(...)
):
    user = next((u for u in users if u["email"] == email), None)
    if not user:
        return {"error": "Invalid email or password"}

    if not bcrypt.checkpw(password.encode('utf-8'), user["password"].encode('utf-8')):
        return {"error": "Invalid email or password"}

    return {"message": f"Welcome, {user['name']}"}
