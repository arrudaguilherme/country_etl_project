from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv('DB_HOST') 
PORT = os.getenv('DB_PORT') 
DB_NAME = os.getenv('DB_NAME') 
USER = os.getenv('DB_USER') 
PASSWORD = os.getenv('DB_PASSWORD') 

POSTGRES_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}'
print(POSTGRES_URL)
engine = create_engine(url=POSTGRES_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine) ## Create database session
## autoflush uodates the db automatically, Set as False, User's choice
## Bind tells that this session refers to this respective engine

Base = declarative_base() ## ORM, inherits making the model, the actual orm is here

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()