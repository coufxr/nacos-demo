from pydantic import Field
from pydantic_settings import BaseSettings


class OpenAIConfig(BaseSettings):
    OPENAI_API_KEY: str = Field(..., description="OPENAI_API_KEY")
    OPENAI_API_BASE: str = Field(..., description="OPENAI_API_BASE")


class QWENConfig(BaseSettings):
    OPENAI_API_BASE: str = Field(..., description="QWEN_OPENAI_API_BASE")


class LocalhostConfig(BaseSettings):
    OPENAI_API_BASE: str = Field(..., description="LOCALHOST_OPENAI_API_BASE")


class DatabaseConfig(BaseSettings):
    DATABASE_HOST: str = Field(..., description="DATABASE_HOST")
    DATABASE_PORT: str = Field(..., description="DATABASE_PORT")
    DATABASE_USER: str = Field(..., description="DATABASE_USER")
    DATABASE_PASSWORD: str = Field(..., description="DATABASE_PASSWORD")
    DATABASE_DBNAME: str = Field(..., description="DATABASE_DBNAME")


class Settings(BaseSettings):
    OPENAI: OpenAIConfig
    QWEN: QWENConfig
    LOCALHOST: LocalhostConfig
    DATABASE: DatabaseConfig


settings: Settings


def get_settings():
    return settings


def set_settings(settings_dict: dict):
    global settings
    settings = Settings(**settings_dict)
