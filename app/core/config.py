from pydantic_settings import BaseSettings,SettingsConfigDict


class Config(BaseSettings):
    app_name:str = "Default name of the app"
    debug:bool
    environment:str
    database_url:str
    model_config=SettingsConfigDict(env_file=".env",extra="ignore")

config=Config()