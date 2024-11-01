from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
fake = Faker('pl_PL')
inspections_table = Table('inspections', metadata, autoload_with=engine)

def add_inspection(fk_ride, fk_inspector, date):
    insert_stmt_inspection = inspections_table.insert().values(fk_ride=fk_ride, fk_inspector=fk_inspector, date=date)
    execute_query(insert_stmt_inspection)

def generate_inspections(how_many):
    for _ in range(how_many):
        add_inspection(fake.random_int(1, 70), fake.random_int(1, 50), fake.date_time_this_year())

if __name__ == '__main__':
    generate_inspections(int(sys.argv[1]))
