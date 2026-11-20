from pydantic import BaseModel,ConfigDict,Field,EmailStr,model_validator
from typing import Annotated
from datetime import datetime,UTC,date
from uuid import uuid4,UUID

class EmployeeBase(BaseModel):
    first_name:str=Field(min_length=2,max_length=50)
    last_name:str=Field(min_length=2,max_length=50)
    email:EmailStr
    department_id:int=Field(gt=0)
    salary:float=Field(gt=0)
    joining_date:date

class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(EmployeeBase):
    first_name:Annotated[str|None,Field(default=None,min_length=2,max_length=50)] =None
    last_name:str|None=Field(default=None,min_length=2,max_length=50)
    email:Annotated[EmailStr|None,Field(default=None)]=None
    department_id:Annotated[int|None,Field(default=None,min_length=1)]=None
    salary:Annotated[float|None,Field(default=None,gt=0)]=None
    joining_date:Annotated[date|None,Field(default=None)]=None

class EmployeeResponse(EmployeeBase):
    eid:UUID
    created_at:datetime
    updated_at:datetime
    model_config=ConfigDict(from_attributes=True)

