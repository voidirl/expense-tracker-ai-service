from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
app = FastAPI()

app.add_middleware(CORSMiddleware,
                   allow_origins=["http://localhost:5173",
                                  "http://localhost:3000",
                                  "https://ai-expense-tracker-frontend-mocha.vercel.app",
                                  "https://voidledger.vercel.app"],
                   allow_methods=["*"],
                   allow_headers=["*"],)

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

class ChatRequest(BaseModel):
    message: str
    expenses: list=[]

@app.post("/chat")
def chat (req: ChatRequest):
    expense_context = ""    
    if req.expenses:
        total = sum(e["amount"] for e in req.expenses)
        expense_context = f"\n\nUser's expenses data:\n"
        for e in req.expenses:
            expense_context += f"- {e['title']} | {e['category']} | ₹{e['amount']} | {e['expenseDate']}\n"
        expense_context += f"Total spent: ₹{total}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{
            "role" : "system",
            "content": f"You're a smart financial advisor for an expense tracker app. Help users understand their spending habits, give budget advice, and answer finance-related questions. Be concise and helpful.{expense_context}"
        },
        {
            "role":"user",
            "content":req.message
        }]
    )

    return {"reply": response.choices[0].message.content}
       
