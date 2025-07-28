
from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Ты — инфо-помощник института IBPS. Отвечай на русском. Говори вежливо, понятно и полезно."},
            {"role": "user", "content": msg.message}
        ]
    )
    return {"reply": response['choices'][0]['message']['content']}
