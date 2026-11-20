from sqlalchemy.orm import Mapped,mapped_column,relationship
from sqlalchemy import String,INT,Numeric,CheckConstraint,ForeignKey,DateTime
from uuid import UUID,uuid4
from datetime import date,datetime,UTC
from app.core.base import Base
from decimal import Decimal


class Employee(Base):
    __tablename__="employees"
    eid:Mapped[UUID]=mapped_column(primary_key=True,default=uuid4)
    first_name:Mapped[str]=mapped_column(String(50),nullable=False)
    last_name:Mapped[str]=mapped_column(String(50),nullable=False)
    email:Mapped[str]=mapped_column(String(255),unique=True,nullable=False)
    salary:Mapped[Decimal]=mapped_column(Numeric(12,2),CheckConstraint("salary > 0",name="check_salary_positive"),nullable=False)
    joining_date:Mapped[date]=mapped_column(nullable=False)
    department_id:Mapped[int]=mapped_column(ForeignKey("departments.id"),nullable=False)
    department= relationship("Department",back_populates="employees")
    created_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda:datetime.now(UTC),nullable=False)
    updated_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda: datetime.now(UTC),onupdate=lambda: datetime.now(UTC),nullable=False)


