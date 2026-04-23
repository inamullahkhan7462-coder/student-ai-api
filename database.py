import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Load environment variables from .env file
load_dotenv()

# 1. DATABASE_URL: Looks for a Cloud URL first, then falls back to your local DB
# This is a professional trick called 'Environment-based configuration'
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:raoinam7462@localhost:5432/student_db")

# 2. Create the Engine
# Note: Render/Postgres often requires 'sslmode=require' for cloud connections
if not DATABASE_URL:
    DATABASE_URL = "postgresql://postgres:raoinam7462@localhost:5432/student_db"
else:
    # Fix for Render's 'postgres://' vs SQLAlchemy's 'postgresql://'
    if DATABASE_URL.startswith("postgres://"):
        DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# 3. Create engine (Added pool_pre_ping to handle cloud hiccups)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# 3. Session and Base (Rest of your code stays the same)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()