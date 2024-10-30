from sqlite3 import connect
from venv import create
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, create_engine
from dotenv import load_dotenv
import os
load_dotenv()
URL = f"postgresql+psycopg2://postgres:{os.environ['POSTGRES_PSSWD']}@localhost:5432/postgres"
engine=create_engine(URL, echo=True)
connection=engine.connect()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Session = sessionmaker(bind=engine)
session = Session()
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()
