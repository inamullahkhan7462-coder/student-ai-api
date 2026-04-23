from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 1. Database Connection URL
# Format: postgresql://username:password@localhost/database_name
DATABASE_URL = "postgresql://postgres:raoinam7462@localhost:5432/student_db"

# 2. Create the Engine (The actual connection)
engine = create_engine(DATABASE_URL)

# 3. Create a Session (How we talk to the DB)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Base Class for our Database Models
Base = declarative_base()

# Helper to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()