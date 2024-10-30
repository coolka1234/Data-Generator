from enum import auto
from math import e
from sqlite3 import connect
from venv import create
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, MetaData, String, create_engine, Table, insert
from dotenv import load_dotenv
import os
load_dotenv()
URL = f"postgresql+psycopg2://postgres:{os.environ['POSTGRES_PSSWD']}@localhost:5432/postgres"
engine=create_engine(URL, echo=True)
connection=engine.connect()
metadata=MetaData()

passenger_table = Table('passenger', metadata, autoload_with=engine)
user_table=Table('app_user', metadata, autoload_with=engine)
insert_stmt_user = insert(user_table).values(id_user=1, login="test", password="test123456", email="jerzy@gmail.com",
                                                phone_number="123456789", name="Jerzy", surname="Kowalski")
# insert_stmt_user = insert(passenger_table).values(id_passenger=1, fk_user=1)


Session = sessionmaker(bind=engine)
session = Session()
with engine.connect() as conn:
    conn.execute(insert_stmt_user)
    conn.commit()

# Querying data from the existing table
result = session.query(user_table).all()
for row in result:
    print(row)
