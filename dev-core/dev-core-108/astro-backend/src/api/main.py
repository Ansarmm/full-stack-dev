from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json

app = FastAPI()
contacts = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ContactForm(BaseModel):
    name: str
    email: str
    phone: int

DATA_FILE = "submissions.json"

def read_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except Exception:
        return []

def write_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

@app.post("/api/contact")
async def receive_contact(form: ContactForm):
    print("Получено сообщение:", form)
    
    all_contacts = read_data()
    all_contacts.append(form.model_dump())
    write_data(all_contacts)

    contacts.append(form.model_dump())

    return {"message": "Сообщение успешно получено"}

@app.get("/api/contact")
def get_contacts():
    return contacts