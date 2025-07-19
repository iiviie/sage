from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from decouple import config

# Get environment-specific configuration
ENV = config('ENV', default='development')
if ENV == 'production':
    DATABASE_URL = config('PROD_DATABASE_URL')
else:
    DATABASE_URL = config('DEV_DATABASE_URL')

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 