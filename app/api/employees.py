from fastapi import APIRouter
from app.schemas.employee import EmployeeCreate

router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"]
)

