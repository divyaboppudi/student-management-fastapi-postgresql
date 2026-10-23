from pydantic import BaseModel


class TeacherStudentResponse(BaseModel):

    id: int

    name: str

    student_class: str

    percentage: float

    model_config = {
        "from_attributes": True
    }