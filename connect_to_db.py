from venv import create
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String, create_engine
URL="jdbc:postgresql://localhost:5432/postgres"
engine=create_engine('sqlite:///example.db', echo=True)

# Define the base model
Base = declarative_base()

# Define a sample model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Create the session factory
Session = sessionmaker(bind=engine)
session = Session()

# Example of querying or adding data
new_user = User(name="Alice", age=30)
session.add(new_user)
session.commit()
