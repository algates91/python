from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel

class BaseConfig(BaseModel):
    port: int
    host: str
    reload: bool

class Configuration(BaseSettings):
    base: BaseConfig

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_nested_delimiter="__")

config = Configuration()

