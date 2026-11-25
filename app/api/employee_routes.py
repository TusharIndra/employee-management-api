from fastapi import APIRouter,status, Depends, Request
from app.schemas.employee_schema import EmployeeCreate,EmployeeResponse,EmployeeUpdate
from app.repositories import employee_repository
from app.models.department_model import Department
from typing import Annotated
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.core.database import get_db
from uuid import UUID
router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"]
)

#static-route
@router.post("/create_user", response_model=EmployeeResponse, status_code=status.HTTP_201_CREATED)
def create_employee_route(emp: EmployeeCreate, db: Annotated[Session,Depends(get_db)]):
    return employee_repository.create_employee(emp,db)

@router.get("/get_all_employees",response_model=list[EmployeeResponse],status_code=status.HTTP_200_OK)
def get_all_employees(db: Annotated[Session,Depends(get_db)]):
    return employee_repository.get_all_employees(db)


@router.get("/by-email",response_model=EmployeeResponse,status_code=status.HTTP_200_OK)
def get_employee_by_email(user_email:str,db: Annotated[Session,Depends(get_db)]):
    return employee_repository.get_employee_by_email(user_email,db)

#dynamic-route
@router.get("/{user_id}",response_model=EmployeeResponse,status_code=status.HTTP_200_OK)
def get_employee_by_id(user_id:UUID,db: Annotated[Session,Depends(get_db)]):
    return employee_repository.get_employee_by_id(user_id,db)

@router.patch("/update-emp/{user_id}",response_model=EmployeeResponse,status_code=status.HTTP_200_OK)
def update_employee(user_id:UUID,db:Annotated[Session,Depends(get_db)],update_element:EmployeeUpdate):
    return employee_repository.update_employee(user_id,db,update_element)

@router.put("/update-emp/{user_id}",response_model=EmployeeResponse,status_code=status.HTTP_200_OK)
def update_full_employee(user_id:UUID,db:Annotated[Session,Depends(get_db)],update_element:EmployeeCreate):
    return employee_repository.update_full_employee(user_id,db,update_element)

@router.delete("/delete/{user_id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_employee(user_id:UUID,db:Annotated[Session,Depends(get_db)]):
    return employee_repository.delete_employee(user_id,db)
