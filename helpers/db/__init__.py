from sqlmodel import create_engine, SQLModel, Session

from .models import Task, Employee # EmployeeCreate #, Employee, Task


DATABASE_URL = "sqlite:///db.sqlite3"


engine = create_engine(DATABASE_URL, echo=True)

def initialize():
    SQLModel.metadata.create_all(engine)  # create tables based models where table is set to True

def get_session():
    with Session(engine) as sess:
        yield sess