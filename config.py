from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    LLM_API_KEY: Optional[str] = None
    LLM_API_BASE: Optional[str] = None
    MODEL_NAME: Optional[str] = None
    SERPER_API_KEY: Optional[str] = None

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

settings = Settings()