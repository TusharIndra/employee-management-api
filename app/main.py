from fastapi import FastAPI,status
from app.core.config import config
from fastapi.responses import JSONResponse
from app.api.employees import router as employee_router

app=FastAPI(title=config.app_name,
            debug=config.debug)

app.include_router(employee_router)

@app.get("/")
def home():
    return JSONResponse(status_code=status.HTTP_200_OK,content={"detail":"successful"})

@app.get("/health")
def health():
    return JSONResponse(status_code=status.HTTP_200_OK,content={"detail":"Healthy"})
