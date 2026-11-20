from app.core.base import Base
from app.core.database import engine
from app.models.department_model import Department
from app.models.employee_model import Employee

Base.metadata.create_all(bind=engine)