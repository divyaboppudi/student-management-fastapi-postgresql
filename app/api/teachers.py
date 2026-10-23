from fastapi import APIRouter
from fastapi import Depends
from fastapi import Query

from app.db.deps import get_db

from app.schemas.teacher import (
    TeacherCreate,
    TeacherResponse
)

from app.schemas.teacher_student import (
    TeacherStudentResponse
)

from app.services.teacher_service import TeacherService


router = APIRouter()

service = TeacherService()


# Create Teacher
@router.post(
    "/teachers",
    response_model=TeacherResponse
)
def create_teacher(
    teacher: TeacherCreate,
    db=Depends(get_db)
):

    return service.create_teacher(
        db,
        teacher
    )


# Get Students Under Teacher
@router.get(
    "/teachers/students",
    response_model=list[TeacherStudentResponse]
)
def get_students_under_teacher(
    teacher_id: str = Query(
        ...,
        description="Teacher ID (positive integer)"
    ),
    db=Depends(get_db)
):

    return service.get_students_under_teacher(
        db,
        teacher_id
    )


# Get Students By Teacher And Class
@router.get(
    "/teachers/students/filter",
    response_model=list[TeacherStudentResponse]
)
def get_students_by_teacher_and_class(
    teacher_id: str = Query(
        ...,
        description="Teacher ID (positive integer)"
    ),
    class_name: str = Query(
        ...,
        description="Class name (e.g. 7A, 8A, 10A)"
    ),
    db=Depends(get_db)
):

    return service.get_students_by_teacher_and_class(
        db,
        teacher_id,
        class_name
    )