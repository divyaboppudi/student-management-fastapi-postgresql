from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi import Request

from app.api.students import router as student_router
from app.api.teachers import router as teacher_router


app = FastAPI(
    title="Student Management API"
)

# Student APIs
app.include_router(student_router)

# Teacher APIs
app.include_router(teacher_router)

#whenever a validation fails, execute this function to handle the error and return a custom response
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(
    request: Request,
    exc: RequestValidationError
):
    error = exc.errors()[0]

    error_type = error.get("type")
    error_location = error.get("loc", [])

    # Handle missing required fields
    if error_type == "missing":

        field_name = error_location[-1]

        friendly_names = {
            "teacher_id": "Teacher ID",
            "class_name": "Class name",
            "student_id": "Student ID",
            "category": "Category",
            "name": "Name",
            "subject": "Subject",
            "percentage": "Percentage"
        }

        field_display_name = friendly_names.get(
            field_name,
            field_name.replace("_", " ").title()
        )

        return JSONResponse(
            status_code=400,
            content={
                "detail": f"{field_display_name} is required"
            }
        )

    error_message = error.get("msg")

    if error_message.startswith("Value error, "):
        error_message = error_message.replace(
            "Value error, ",
            ""
        )

    return JSONResponse(
        status_code=400,
        content={
            "detail": error_message
        }
    )