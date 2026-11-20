from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,INT
from app.core.base import Base


class Department(Base):
    __tablename__="departments"
    id:Mapped[int]=mapped_column(INT,primary_key=True)
    name:Mapped[str]=mapped_column(String(100),unique=True,nullable=False)
    description:Mapped[str|None]=mapped_column(String(255),default=None)

    employees=relationship("Employee",back_populates="department")

