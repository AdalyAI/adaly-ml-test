from pydantic_settings import BaseSettings
import os
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    """Application settings."""
    
    # Application
    APP_NAME: str = "Library API"
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    API_PREFIX: str = os.getenv("API_PREFIX", "/api/v1")
    
    # Database
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    
    class Config:
        env_file = ".env"


settings = Settings()