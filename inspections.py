from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
fake = Faker('pl_PL')
inspections_table = Table('inspections', metadata, autoload_with=engine)

def add_inspection(distance, number_of_stops, estimated_travel_time):
    insert_stmt_path = inspections_table.insert().values(distance=distance, number_of_stops=number_of_stops, estimated_travel_time=estimated_travel_time)
    execute_query(insert_stmt_path)

def generate_inspections(how_many):
    for _ in range(how_many):
        add_inspection(fake.random_int(1, 1000), fake.random_int(3, 30), fake.random_int(1, 1000))

if __name__ == '__main__':
    generate_inspections(int(sys.argv[1]))
