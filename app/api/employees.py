from fastapi import APIRouter
from app.schemas.employee import EmployeeCreate
import json
router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"]
)


emplist:list[dict] =[{
        "first_name":"Mandy",
        "last_name":"singh",
        "email":"mandysingh@gmail.com",
        "department":"IT",
        "salary":20000.20,
        "joining_date":"2025-04-02"
    },
    {
        "first_name":"candy",
        "last_name":"singh",
        "email":"candusingh@gmail.com",
        "department":"IT",
        "salary":40000.20,
        "joining_date":"2025-01-01"
    }
    ]


@router.post("/validate")
def validate_employee(employee: EmployeeCreate):
    emplist.append(employee.model_dump(mode="json"))
    return employee.model_dump(mode="json")

@router.get("/getall")
def return_all():
    return emplist
