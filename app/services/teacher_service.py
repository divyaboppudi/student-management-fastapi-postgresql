from fastapi import HTTPException
import re

from app.repositories.teacher_repo import TeacherRepository


class TeacherService:

    def __init__(self):
        self.repo = TeacherRepository()

    # Create Teacher
    def create_teacher(
        self,
        db,
        teacher_data
    ):

        existing_teacher = (
            self.repo.get_teacher_by_details(
                db,
                teacher_data.name,
                teacher_data.subject,
                teacher_data.class_name
            )
        )

        if existing_teacher:
            raise HTTPException(
                status_code=409,
                detail="Teacher already exists for this subject and class"
            )

        return self.repo.create_teacher(
            db,
            teacher_data
        )

    # Get Teacher By ID
    def get_teacher_by_id(
        self,
        db,
        teacher_id
    ):

        if not teacher_id:
            raise HTTPException(
                status_code=400,
                detail="Teacher ID must be a valid positive integer"
            )

        if isinstance(teacher_id, str):

            teacher_id = teacher_id.strip()

            if not teacher_id:
                raise HTTPException(
                    status_code=400,
                    detail="Teacher ID must be a valid positive integer"
                )

            if not teacher_id.isdigit():
                raise HTTPException(
                    status_code=400,
                    detail="Teacher ID must be a valid positive integer"
                )

            teacher_id = int(teacher_id)

        if teacher_id <= 0:
            raise HTTPException(
                status_code=400,
                detail="Teacher ID must be a valid positive integer"
            )

        teacher = self.repo.get_teacher_by_id(
            db,
            teacher_id
        )

        if not teacher:
            raise HTTPException(
                status_code=404,
                detail="Teacher not found"
            )

        return teacher

    # Get Students Under Teacher
    def get_students_under_teacher(
        self,
        db,
        teacher_id
    ):

        teacher = self.get_teacher_by_id(
            db,
            teacher_id
        )

        students = self.repo.get_students_by_teacher(
            db,
            teacher.class_name
        )

        if not students:
            raise HTTPException(
                status_code=404,
                detail="No students found under this teacher"
            )

        return students

    # Get Students By Teacher And Class
    def get_students_by_teacher_and_class(
        self,
        db,
        teacher_id,
        class_name
    ):

        teacher = self.get_teacher_by_id(
            db,
            teacher_id
        )

        class_name = class_name.strip()

        if not class_name:
            raise HTTPException(
                status_code=400,
                detail="Class name cannot be empty"
            )

        if class_name.lower() in ["null", "none"]:
            raise HTTPException(
                status_code=400,
                detail="Class name cannot be null"
            )

        if not re.fullmatch(r"\d+[A-Za-z]", class_name):
            raise HTTPException(
                status_code=400,
                detail="Invalid class name. Expected format: Number followed by a letter (e.g. 7A, 8A, 10A)"
            )

        if teacher.class_name.lower() != class_name.lower():
            raise HTTPException(
                status_code=400,
                detail=f"Teacher is not assigned to class {class_name}"
            )

        students = self.repo.get_students_by_teacher_and_class(
            db,
            class_name
        )

        if not students:
            raise HTTPException(
                status_code=404,
                detail="No students found for the given class"
            )

        return students