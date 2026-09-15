from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
import os

load_dotenv()
client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Expense(BaseModel):
    amount: float
    category: str

class InsightRequest(BaseModel):
    expenses: list[Expense]
    budget: float

@app.get("/")
def read_root():
    return {"message": "Budget Tracker API is running"}

@app.post("/insight")
def get_insight(data: InsightRequest):
    expense_summary = ", ".join(
        [f"{e.category}: ₦{e.amount}" for e in data.expenses]
    )

    prompt = f"""You are a friendly budget advisor. A user has a monthly budget of ₦{data.budget}.
Their expenses so far: {expense_summary}.
Give one short, encouraging tip (2-3 sentences max) about their spending."""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    return {"insight": response.text}