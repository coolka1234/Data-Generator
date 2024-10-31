from sqlalchemy import MetaData, create_engine, Table, insert
from dotenv import load_dotenv
import os
load_dotenv()
URL = f"postgresql+psycopg2://postgres:{os.environ['POSTGRES_PSSWD']}@localhost:5432/postgres"
engine=create_engine(URL, echo=True)
connection=engine.connect()
metadata=MetaData()

# user_table=Table('app_user', metadata, autoload_with=engine)
# insert_stmt_user = insert(user_table).values(id_user=3, login="test23", password="test1234563", email="f2ranek@gmail.com",
#                                              phone_number="123456783", name="Krycha", surname="Kowalski")

def execute_query(query):
    with engine.connect() as conn:
        conn.execute(query)
        conn.commit()
