from pydantic import Field
from pydantic_settings import BaseSettings


class OpenAIConfig(BaseSettings):
    OPENAI_API_KEY: str = Field(..., description="OPENAI_API_KEY")
    OPENAI_API_BASE: str = Field(..., description="OPENAI_API_BASE")


class QWENConfig(BaseSettings):
    OPENAI_API_BASE: str = Field(..., description="QWEN_OPENAI_API_BASE")


class LOCALHOSTConfig(BaseSettings):
    OPENAI_API_BASE: str = Field(..., description="LOCALHOST_OPENAI_API_BASE")


class Settings(BaseSettings):
    OPENAI: OpenAIConfig
    QWEN: QWENConfig
    LOCALHOST: LOCALHOSTConfig


settings: Settings


def get_settings():
    return settings


def set_settings(settings_dict: dict):
    global settings
    settings = Settings(**settings_dict)
