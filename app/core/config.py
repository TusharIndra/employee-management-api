from pydantic_settings import BaseSettings
from dotenv import load_dotenv
load_dotenv()

class Config(BaseSettings):
    app_name:str = "Default name of the app"
    debug:bool
    environment:str

config=Config()