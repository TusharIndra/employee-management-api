from pydantic_settings import SettingsConfigDict,BaseSettings

class Settings(BaseSettings):
    app_name:str = "Default name of the app"
    debug:bool
    environment:str

    model_config=SettingsConfigDict(env_file=".env", extra="ignore")