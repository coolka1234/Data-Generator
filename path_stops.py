from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table
from faker import Faker
import sys
fake = Faker('pl_PL')
path_stops_table = Table('path_stops', metadata, autoload_with=engine)

def add_path_stops(id_path, id_stop, path_minute):
    insert_stmt_ps = path_stops_table.insert().values(id_path=id_path, id_stop=id_stop, path_minute=path_minute)
    execute_query(insert_stmt_ps)

def generate_path_stops(how_many):
    for _ in range(how_many):
        add_path_stops(fake.random_int(1, 210), fake.random_int(1, 100), fake.random_int(1, 1000))


if __name__ == '__main__':
    generate_path_stops(int(sys.argv[1]))