from fastapi import FastAPI, Body

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

    if not name or not email or not password:
        return {"message": "All fields should be filled"}

    if len(password) <= 6:
        return {"message": "Password should be longer than 6 characters"}

    new_user = {
        "id": len(users) + 1,
        "name": name,
        "email": email,
        "password": password,
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
    if not user or user["password"] != password:
        return {"error": "Invalid email or password"}

    return {"message": f"Welcome, {user['name']}"}
