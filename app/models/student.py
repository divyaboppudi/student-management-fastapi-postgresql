# Column data types
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Float

# Base class from session.py
from app.db.session import Base


# Student table
class Student(Base):

    # Table name in PostgreSQL
    __tablename__ = "students"

    # Primary Key
    # PostgreSQL will auto-generate values:
    # 1, 2, 3, 4...
    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    # Student name
    name = Column(
        String,
        nullable=False
    )

    # Student class
    student_class = Column(
        String,
        nullable=False
    )

    # Student percentage

    percentage = Column(
        Float,
        nullable=False
    )