from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = "postgresql+asyncpg://user:password@localhost:5432/dbname"
    DB_ECHO: bool = False
    APP_HOST: str = "0.0.0.0"
    APP_PORT: str = 8001

    class Config:
        env_file = ".env"


settings = Settings()
