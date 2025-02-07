from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

db_user = os.getenv('DB_USER')
db_password = os.getenv('DB_PASSWORD')
db_name = os.getenv('DB_NAME')

POSTGRES_DATABASE_URL = f"postgresql://{db_user}:{db_password}@postgres/{db_name}"

engine = create_engine(POSTGRES_DATABASE_URL)

SessionLocal = sessionmaker (autocommit= True, autoflush= False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()