from pydantic_settings import BaseSettings
import os

class Settings(BaseSettings):
    PROJECT_NAME: str = "FastAPI Project"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./sql_app.db")

    class Config:
        env_file = ".env"

settings = Settings()