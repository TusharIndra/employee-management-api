from fastapi import FastAPI
from core.config import Settings

settings=Settings()

app=FastAPI(title=settings.app_name,
            debug=settings.debug)

@app.get("/")
def home():
    return {"APP_NAME":settings.app_name}

@app.get("/health")
def health():
    return {"status": "healthy"}
