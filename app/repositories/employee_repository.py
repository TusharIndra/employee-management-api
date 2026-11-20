from app.core.database import get_db
from app.models.department_model import Department
from app.models.employee_model import Employee
from typing import Annotated
from app.schemas.employee_schema import EmployeeCreate,EmployeeResponse
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends,HTTPException,status
from uuid import UUID

#create new user in the database
def create_employee(emp:EmployeeCreate,db:Annotated[Session,Depends(get_db)]):
    result = db.execute(select(Employee).where(Employee.email == emp.email))
    user=result.scalars().first()

    #create exception here
    if user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exisiting"
        )

    #creation of new employee
    new_user=Employee(
        **emp.model_dump()
    )

    #inserting into db
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

#get employee details by eid
def get_employee_by_id(user_id:UUID, db:Annotated[Session,Depends(get_db)]):
    user=db.get(Employee,user_id)
    #exception here
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

#get all employee details
def get_all_employees(db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(Employee))
    users = result.scalars().all()
    return users

#get employee detail by email
def get_employee_by_email(user_mail:str,db:Annotated[Session,Depends(get_db)]):
    result=db.execute(select(Employee).where(Employee.email==user_mail))
    user=result.scalars().first()
    #exception here
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user



def update_employee(db:Annotated[Session,Depends(get_db)]):
    pass

def delete_employee(db:Annotated[Session,Depends(get_db)]):
    pass

