from fastapi import HTTPException
import re

# Repository
from app.repositories.student_repo import StudentRepository

# Student Model
from app.models.student import Student


class StudentService:

    def __init__(self):
        self.repo = StudentRepository()

    # Create Student
    def create_student(
        self,
        db,
        student_data
    ):
        return self.repo.create_student(
            db,
            student_data
        )

    # Get Students By Class
    def get_students_by_class(
        self,
        db,
        class_name
    ):

        if not class_name:
            raise HTTPException(
                status_code=400,
                detail="Class name cannot be empty"
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

        students = self.repo.get_students_by_class(
            db,
            class_name
        )

        if not students:
            raise HTTPException(
                status_code=404,
                detail="No students found for the given class"
            )

        return students

    # Get Specific Student
    def get_student(
        self,
        db,
        student_id=None,
        name=None,
        class_name=None
    ):

        if not student_id and not name and not class_name:
            raise HTTPException(
                status_code=400,
                detail="Provide student_id or both name and class_name"
            )

        if student_id:

            student = self.repo.get_student(
                db,
                student_id,
                name,
                class_name
            )

            if not student:
                raise HTTPException(
                    status_code=404,
                    detail="Student not found"
                )

            return student

        if not name or not name.strip():
            raise HTTPException(
                status_code=400,
                detail="Name cannot be empty"
            )

        if not class_name or not class_name.strip():
            raise HTTPException(
                status_code=400,
                detail="Class name cannot be empty"
            )

        name = name.strip()
        class_name = class_name.strip()

        if name.lower() in ["null", "none"]:
            raise HTTPException(
                status_code=400,
                detail="Name cannot be null"
            )

        if class_name.lower() in ["null", "none"]:
            raise HTTPException(
                status_code=400,
                detail="Class name cannot be null"
            )

        if not re.fullmatch(r"[A-Za-z ]+", name):
            raise HTTPException(
                status_code=400,
                detail="Name contains invalid characters"
            )

        if not re.fullmatch(r"\d+[A-Za-z]", class_name):
            raise HTTPException(
                status_code=400,
                detail="Invalid class name. Expected format: Number followed by a letter (e.g. 7A, 8A, 10A)"
            )

        student = self.repo.get_student(
            db,
            student_id,
            name,
            class_name
        )

        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return student

    # Get Student By ID
    def get_student_by_id(
        self,
        db,
        student_id
    ):

        if not student_id:
            raise HTTPException(
                status_code=400,
                detail="Student ID must be a valid positive integer"
            )

        student_id = student_id.strip()

        if not student_id:
            raise HTTPException(
                status_code=400,
                detail="Student ID must be a valid positive integer"
            )

        if not student_id.isdigit():
            raise HTTPException(
                status_code=400,
                detail="Student ID must be a valid positive integer"
            )

        student_id = int(student_id)

        if student_id <= 0:
            raise HTTPException(
                status_code=400,
                detail="Student ID must be a valid positive integer"
            )

        student = self.repo.get_student_by_id(
            db,
            student_id
        )

        if not student:
            raise HTTPException(
                status_code=404,
                detail="Student not found"
            )

        return student

    # Get Students By Result Category
    def get_students_by_result(
        self,
        db,
        category
    ):

        if not category:
            raise HTTPException(
                status_code=400,
                detail="Category cannot be empty"
            )

        category = category.strip()

        if not category:
            raise HTTPException(
                status_code=400,
                detail="Category cannot be empty"
            )

        if category.lower() in ["null", "none"]:
            raise HTTPException(
                status_code=400,
                detail="Category cannot be null"
            )

        category = category.lower()

        if category == "distinction":

            return self.repo.get_students_by_percentage(
                db,
                70
            )

        elif category == "firstclass":

            return self.repo.get_students_by_percentage(
                db,
                60,
                69
            )

        elif category == "secondclass":

            return self.repo.get_students_by_percentage(
                db,
                50,
                59
            )

        elif category == "fail":

            return (
                db.query(Student)
                .filter(Student.percentage < 50)
                .all()
            )

        else:
            raise HTTPException(
                status_code=400,
                detail="Invalid category. Allowed values: distinction, firstclass, secondclass, fail"
            )