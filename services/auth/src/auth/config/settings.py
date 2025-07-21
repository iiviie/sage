from functools import lru_cache
from typing import Literal
from pydantic_settings import BaseSettings
from pydantic import PostgresDsn

class Settings(BaseSettings):
    # Environment
    ENV: Literal["development", "production"] = "development"
    
    # Database Settings
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str = "auth_db"  # default to docker-compose service name
    POSTGRES_PORT: int = 5432
    
    @property
    def DATABASE_URL(self) -> PostgresDsn:
        """Dynamically construct database URL based on environment."""
        return PostgresDsn.build(
            scheme="postgresql",
            username=self.POSTGRES_USER,
            password=self.POSTGRES_PASSWORD,
            host=self.POSTGRES_HOST,
            port=self.POSTGRES_PORT,
            path=self.POSTGRES_DB,
        )

    # JWT Settings
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    # Application Settings
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "Auth Service"
    DEBUG: bool = False

    class Config:
        env_file = ".env"
        case_sensitive = True

@lru_cache
def get_settings() -> Settings:
    """
    Get settings instance with caching.
    
    Returns:
        Settings: Application settings instance
    """
    return Settings()

# Create a global settings instance
settings = get_settings() 