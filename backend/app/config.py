from pathlib import Path

from pydantic import BaseModel, SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    APP_HOST: str = "http://localhost:5173/"

    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: int = 5432
    DATABASE_USERNAME: str = "postgres"
    DATABASE_PASSWORD: SecretStr = "postgres"
    DATABASE_DB: str = "kinoxata"

    GOOGLE_CLIENT_ID: str = "1036942335380-fd7f5iu3f8e4v00sgjhood02tf04g0lh.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET: str = "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"


settings = Settings()
