from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

# Get database URL from environment variable with a default for local development
DATABASE_URL = config(
    'DATABASE_URL',
    default='postgresql://postgres:postgres@localhost:5432/auth_db'
)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 