from typing import List, Optional
import datetime
from sqlmodel import Relationship, SQLModel, Field, DateTime


class TaskBase(SQLModel):
    name: str
    category: str
    # employee: "Employee" = Relationship(back_populates="tasks")


class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime.datetime
    employee_id: int = Field(foreign_key="employee.id")



class EmployeeBase(SQLModel):
    name: str
    title: str


class Employee(EmployeeBase, table=True):
    id: int = Field(default=None, primary_key=True)
    created_at: datetime.datetime
    tasks: List[Task] = Relationship(back_populates="employee")

# class EmployeeCreate(EmployeeBase):
#     tasks: Optional[List[Task]] = None
    
