from fastapi import FastAPI,status,Depends,HTTPException
from app.core.config import config
from fastapi.responses import JSONResponse
from app.api.employee_routes import router as employee_router
from sqlalchemy import text
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from app.core.database import get_db

app=FastAPI()

app.include_router(employee_router)

@app.get("/")
def home():
    return JSONResponse(status_code=status.HTTP_200_OK,content={"detail":"successful"})

@app.get("/health")
def health():
    return JSONResponse(status_code=status.HTTP_200_OK,content={"detail":"Healthy"})

@app.get("/db_health")
def db_health(db:Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT 1")).scalar_one()
        if result != 1:
            raise HTTPException(
                status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
                detail="Database unavailable"
            )

        return {"database": "connected"}

    except SQLAlchemyError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database unavailable"
        )
