from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
import json
from json import JSONDecodeError

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Feedback(BaseModel):
    name: str
    email: str
    message: str

def load_feedback():
    with open("feedback.json", "r") as f:
        return json.load(f)


def save_feedback(data):
    with open("feedback.json", "w") as f:
        json.dump(data, f, indent=2)

@app.post("/feedback")
async def submit_feedback(feedback: Feedback):
    feedbacks = load_feedback()
    entry = {
        "name": feedback.name,
        "email": feedback.email,
        "message": feedback.message,
        "timestamp": datetime.now().isoformat()
    }
    feedbacks["feedbacks"].append(entry)
    save_feedback(feedbacks)
    return {"message": "Feedback submitted successfully"}

@app.get("/feedback")
async def get_all_feedback():
    feedbacks = load_feedback()
    return feedbacks
