from contextlib import asynccontextmanager
from fastapi import FastAPI, HTTPException, Path, Query, Depends
from ..import db
# from ..db.models import EmployeeCreate, Employee, Task


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.initialize()
    yield
    

app = FastAPI(lifespan=lifespan)



@app.get("/employees")
async def create_employee():
    return [1, 2, 3]
