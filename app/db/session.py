# Creates a connection (engine) to PostgreSQL
from sqlalchemy import create_engine

# Base class for all database tables/models
from sqlalchemy.orm import declarative_base

# Creates database sessions
from sqlalchemy.orm import sessionmaker


# PostgreSQL connection string
#
# Format:
# postgresql+psycopg://username:password@host:port/database
#
DATABASE_URL = (
    "postgresql+psycopg://"
    "postgres:postgres123@localhost:5433/"
    "student_management"
)

# Engine = Actual connection to PostgreSQL
engine = create_engine(DATABASE_URL)


# SessionLocal creates database sessions
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


# Base class for all database models
#
# Every table will inherit from Base
#
# Example:
#
# class Student(Base):
#     __tablename__ = "students"
#
Base = declarative_base()