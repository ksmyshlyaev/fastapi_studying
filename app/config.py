from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv("../.env"))


class DBSettings(BaseSettings):
    # DB credentials
    HOST: str
    PORT: int
    NAME: str
    USER: str
    PASS: str
    model_config = SettingsConfigDict(env_prefix="db_")
