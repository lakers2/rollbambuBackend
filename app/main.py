from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.endpoints import items, fortune
from app.core.config import settings
from app.db.database import create_tables
from init_db import init_db

app = FastAPI(title=settings.PROJECT_NAME)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有来源，仅用于测试
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router, prefix="/api")
app.include_router(fortune.router, prefix="/api")

@app.on_event("startup")
async def startup_event():
    create_tables()
    init_db()

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}