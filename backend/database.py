from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

POSTGRES_DATABASE_URL = "postgresql://user:password@postgres/mydatabase"
engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush= False, bind=engine)

Base = declarative_base() #ORM


def get_db():
    db = SessionLocal()
    try:
        yield db #yield é tipo um return mas não morre a função, pode chamar varias vezes.
    finally:
        db.close()