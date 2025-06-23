from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()
contacts = []

class ContactForm(BaseModel):
    name: str
    email: str
    phone: str
    message: str

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

DATA_FILE = "data.json"

def read_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def write_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

@app.post("/api/contact")
async def receive_contact(form: ContactForm):
    print("Получено сообщение:", form)
    
    all_contacts = read_data()
    all_contacts.append(form.dict())
    write_data(all_contacts)

    contacts.append(form.dict())

    return {"message": "Сообщение успешно получено"}

@app.get("/api/contact")
def get_contacts():
    return contacts
