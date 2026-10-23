from app.models.teacher import Teacher


class TeacherRepository:

    # Create Teacher
    def create_teacher(
        self,
        db,
        teacher_data
    ):

        teacher = Teacher(
            name=teacher_data.name,
            subject=teacher_data.subject,
            class_name=teacher_data.class_name
        )

        db.add(teacher)

        db.commit()

        db.refresh(teacher)

        return teacher

    # Check Duplicate Teacher
    def get_teacher_by_details(
        self,
        db,
        name,
        subject,
        class_name
    ):

        return (
            db.query(Teacher)
            .filter(
                Teacher.name.ilike(name),
                Teacher.subject.ilike(subject),
                Teacher.class_name.ilike(class_name)
            )
            .first()
        )

    # Get Teacher By ID
    def get_teacher_by_id(
        self,
        db,
        teacher_id
    ):

        return (
            db.query(Teacher)
            .filter(
                Teacher.id == teacher_id
            )
            .first()
        )

    # Get Students Under Teacher
    def get_students_by_teacher(
        self,
        db,
        class_name
    ):

        from app.models.student import Student

        return (
            db.query(Student)
            .filter(
                Student.student_class == class_name
            )
            .all()
        )

    # Get Students By Teacher And Class
    def get_students_by_teacher_and_class(
        self,
        db,
        class_name
    ):

        from app.models.student import Student

        return (
            db.query(Student)
            .filter(
                Student.student_class == class_name
            )
            .all()
        )