# Imports Base and engine
from app.db.session import Base
from app.db.session import engine

# Import Student model
from app.models.student import Student

# Import Teacher model
from app.models.teacher import Teacher


# Create all tables in PostgreSQL
Base.metadata.create_all(bind=engine)

print("Tables created successfully")