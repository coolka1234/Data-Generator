from enum import auto
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

passanger_table = Table('passanger', metadata, autoload_with=engine)

insert_stmt = insert(passanger_table).values(id_passanger=1, fk_user=1)

Session = sessionmaker(bind=engine)
session = Session()
with engine.connect() as conn:
    conn.execute(insert_stmt)
    conn.commit()

# Querying data from the existing table
result = session.query(passanger_table).all()
for row in result:
    print(row)
