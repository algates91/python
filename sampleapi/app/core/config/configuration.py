from pathlib import Path
from typing import Type
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict, TomlConfigSettingsSource
from pydantic import BaseModel

class BaseConfig(BaseModel):
    host: str
    port: int
    name: str
    version: str

class DatabaseConfig(BaseModel):
    username: str
    password: str
    database_name: str
    database_url: str

class JWTconfig(BaseModel):
    secret: str
    algorithm: str
    expiry: int

class Configuration(BaseSettings):
    base: BaseConfig
    database: DatabaseConfig
    jwt: JWTconfig
    # Use an absolute path to the TOML so loading is consistent regardless
    # of the current working directory when the process is started.
    _toml_path = Path(__file__).resolve().parents[3] / ".secrets" / "config.toml"
    model_config = SettingsConfigDict(toml_file=str(_toml_path))
    
    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: Type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls),)

config = Configuration()
    