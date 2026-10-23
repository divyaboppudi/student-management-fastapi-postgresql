# Database Session
from app.db.session import SessionLocal


# Dependency
def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()