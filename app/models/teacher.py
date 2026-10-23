from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String

from app.db.session import Base


class Teacher(Base):

    __tablename__ = "teachers"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    subject = Column(
        String,
        nullable=False
    )

    class_name = Column(
        String,
        nullable=False
    )