from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Sage API", version="1.0.0")

@app.get("/{name}")
async def hello(name: str):
    return {"hello": name} 