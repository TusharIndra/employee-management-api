from app.core.database import get_db
from app.models.department_model import Department
from app.models.employee_model import Employee
from typing import Annotated
from app.schemas.employee_schema import EmployeeCreate,EmployeeResponse, EmployeeUpdate
from sqlalchemy.orm import Session
from sqlalchemy import select
from fastapi import Depends,HTTPException,status
from sqlalchemy.exc import IntegrityError
from uuid import UUID

#create new user in the database
def create_employee(emp:EmployeeCreate,db:Session):
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
    try:
        db.add(new_user)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,detail="Error creating Employee")
    
    db.refresh(new_user)
    return new_user

#get employee details by eid
def get_employee_by_id(user_id:UUID, db:Session):
    user=db.get(Employee,user_id)
    #exception here
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

#get all employee details
def get_all_employees(db:Session):
    result=db.execute(select(Employee))
    users = result.scalars().all()
    return users

#get employee detail by email
def get_employee_by_email(user_mail:str,db:Session):
    result=db.execute(select(Employee).where(Employee.email==user_mail))
    user=result.scalars().first()
    #exception here
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    return user


#patch method used
def update_employee(user_id:UUID,db:Session,update_element:EmployeeUpdate):
    updated_employee=db.scalars(select(Employee).where(Employee.eid==user_id)).one_or_none()
    if not updated_employee:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
    else:
        update_data=update_element.model_dump(exclude_unset=True)
        for key, item in update_data.items():
            setattr(updated_employee,key,item)

    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="An employee with this email already exists",
            )
    
    db.refresh(updated_employee)
    return updated_employee

#put method used
def update_full_employee(user_id:UUID,db:Session,update_element:EmployeeCreate):
    updated_employee=db.scalars(select(Employee).where(Employee.eid==user_id)).one_or_none()
    if not updated_employee:
        raise HTTPException(
                    status_code=status.HTTP_404_NOT_FOUND,
                    detail="User not found"
                )
    else:
        update_data=update_element.model_dump()
        for key, item in update_data.items():
            setattr(updated_employee,key,item)
    try:
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="An employee with this email already exists",
        )
    db.refresh(updated_employee)
    return updated_employee


def delete_employee(user_id:UUID,db:Session):
    employee_to_be_deleted=db.scalars(select(Employee).where(Employee.eid==user_id)).one_or_none()
    if not employee_to_be_deleted:
        raise HTTPException(status_code=404,detail="Employee not found")
    try:
        db.delete(employee_to_be_deleted)
        db.commit()
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=409,detail="Cannot delete employee")

    return
