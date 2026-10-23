from sqlalchemy import func

# Student table
from app.models.student import Student


class StudentRepository:

    # Add a single student
    def create_student(
        self,
        db,
        student_data
    ):

        # Create Student object
        student = Student(
            name=student_data.name,
            student_class=student_data.student_class,
            percentage=student_data.percentage
        )

        # Track object
        db.add(student)

        # Save to PostgreSQL
        db.commit()

        # Reload latest values from DB
        db.refresh(student)

        return student

    # Get all students by class
    def get_students_by_class(
        self,
        db,
        class_name
    ):

        return (
            db.query(Student)
            .filter(
                func.lower(Student.student_class)
                == class_name.lower()
            )
            .all()
        )

    # Get specific student
    def get_student(
        self,
        db,
        student_id=None,
        name=None,
        class_name=None
    ):

        # Search by ID
        if student_id:

            return (
                db.query(Student)
                .filter(
                    Student.id == student_id
                )
                .first()
            )

        # Search by Name + Class
        return (
            db.query(Student)
            .filter(
                func.lower(Student.name)
                == name.lower(),

                func.lower(Student.student_class)
                == class_name.lower()
            )
            .first()
        )

    # Get students by percentage range
    def get_students_by_percentage(
        self,
        db,
        min_percentage,
        max_percentage=None
    ):

        query = db.query(Student)

        if max_percentage is not None:

            query = query.filter(
                Student.percentage >= min_percentage,
                Student.percentage <= max_percentage
            )

        else:

            query = query.filter(
                Student.percentage >= min_percentage
            )

        return query.all()

    # Get student by ID
    def get_student_by_id(
        self,
        db,
        student_id
    ):

        return (
            db.query(Student)
            .filter(
                Student.id == student_id
            )
            .first()
        )