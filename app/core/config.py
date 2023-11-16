import os
from typing import List

from dotenv import load_dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

load_dotenv()


class BaseAppSettings(BaseSettings):
    # base
    ENV: str = "local"
    API: str = "/api"
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "test-api"

    PROJECT_ROOT: str = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )

    # date
    DATETIME_FORMAT: str = "%Y-%m-%dT%H:%M:%S"
    DATE_FORMAT: str = "%Y-%m-%d"

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = ["*"]

    COIN_API_TOKEN: str

    class Config:
        case_sensitive = True


class LocalSettings(BaseAppSettings):
    ENV: str = "local"


class TestSettings(BaseAppSettings):
    ENV: str = "test"


class ProdSettings(BaseAppSettings):
    ENV: str = "prod"


def get_scope() -> str:
    return os.getenv("ENV", "local")


def get_config() -> BaseAppSettings:
    env = get_scope()
    config_type: dict[str, BaseAppSettings] = {
        "test": TestSettings(),
        "local": LocalSettings(),
        "prod": ProdSettings(),
    }
    return config_type[env]


settings: BaseAppSettings = get_config()
