from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "Vizsale-fastapi"
    api_v1_prefix: str = "/api/v1"
    max_file_size_mb: int = 10
    allowed_origins: list[str] = ["http://localhost:3000"]

    class Config:
        env_file = ".env"

settings = Settings()