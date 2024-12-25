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

    PRIVATE_KEY: str = ("-----BEGIN PRIVATE KEY-----\n"
                        "MC4CAQAwBQYDK2VwBCIEIH7sjlQYpBCnodJqPqYS2441L4wOOqyfLoc/SzTTC1h8"
                        "\n-----END PRIVATE KEY-----\n")
    PUBLIC_KEY: str = ("-----BEGIN PUBLIC KEY-----\n"
                       "MCowBQYDK2VwAyEALBpYeqDs0G6ozySYWUx999Ig7Ebj6SQ7y6TfhY+aI+U="
                       "\n-----END PUBLIC KEY-----\n")

    GOOGLE_CLIENT_ID: str = "you_id"
    GOOGLE_CLIENT_SECRET: str = "you_secret"


settings = Settings()
