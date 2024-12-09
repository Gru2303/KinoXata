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
    GOOGLE_LOGIN_URL: str = ("https://accounts.google.com/o/oauth2/v2/auth?client_id={GOOGLE_CLIENT_ID}&"
                             "response_type=code&scope=openid%20email%20profile&"
                             "redirect_uri=http://localhost:8000/api/v1/login/google/callback")


settings = Settings()
