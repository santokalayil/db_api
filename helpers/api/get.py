from . import app


# @app.get(/)


@app.get("/employees")
async def create_employee(employee_data):
    return [1, 2, 3]


