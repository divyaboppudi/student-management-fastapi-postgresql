# Creates API routes
from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

# Database Dependency
from app.db.deps import get_db

# Request and Response Schemas
from app.schemas.student import (
    StudentCreate,
    StudentResponse
)

# Service Layer
from app.services.student_service import StudentService


# Creates router object
router = APIRouter()

# Creates service object
service = StudentService()


# Create Student API
@router.post(
    "/students",
    response_model=StudentResponse
)
def create_student(
    student: StudentCreate,
    db=Depends(get_db)
):

    return service.create_student(
        db,
        student
    )


# Get all students by class
@router.get(
    "/students"
)
def get_students_by_class(
    class_name: str = None,
    db=Depends(get_db)
):

    return service.get_students_by_class(
        db,
        class_name
    )


# Get specific student
@router.get(
    "/student"
)
def get_student(
    student_id: int = None,
    name: str = None,
    class_name: str = None,
    db=Depends(get_db)
):

    return service.get_student(
        db,
        student_id,
        name,
        class_name
    )


# Get students by result category
@router.get(
    "/students/result"
)
def get_students_by_result(
    category: str = Query(
        ...,
        description="""
Allowed values:

- distinction → percentage >= 70
- firstclass → percentage between 60 and 69
- secondclass → percentage between 50 and 59
- fail → percentage < 50
"""
    ),
    db=Depends(get_db)
):

    return service.get_students_by_result(
        db,
        category
    )


# Get Student By ID
@router.get(
    "/students/{student_id}"
)
def get_student_by_id(
    student_id: str,
    db=Depends(get_db)
):

    return service.get_student_by_id(
        db,
        student_id
    )