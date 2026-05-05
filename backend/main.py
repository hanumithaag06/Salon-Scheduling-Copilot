from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import text
from database import engine

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/services")
def get_services():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM services"))
        return [dict(row._mapping) for row in result]