from sqlalchemy import MetaData, create_engine, Table, insert
from dotenv import load_dotenv
import os
from ticket_types import load_ticket_types
from sqlalchemy import text


load_dotenv()
# enter your database connection here "postgresql+psycopg2://[USER]:[PASSWORD]@localhost:5432/[DATABASE NAME]"
URL = f"postgresql+psycopg2://postgres:postgres@localhost:5432/MPK"
engine = create_engine(URL, echo=True)
connection = engine.connect()
metadata = MetaData()


def create_tables():
    path = "ddl.sql"
    with open(path, "r") as file:
        query = file.read()
        for command in query.split(";"):
            if command.strip():
                execute_query(text(command))
    load_ticket_types()


def execute_query(query):
    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()


if __name__ == "__main__":
    create_tables()
