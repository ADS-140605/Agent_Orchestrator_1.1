from fastapi import FastAPI
from app.database import get_db, engine, Base


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
