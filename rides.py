from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
from fk_keys_hash_sets import load_set, save_set, path_fk_keys_set, line_numbers_set
fake = Faker('pl_PL')
rides_table = Table('rides', metadata, autoload_with=engine)

def add_ride(fk_line, fk_path, fk_vehicle, fk_driver, weekday, time):
    insert_stmt_ride = rides_table.insert().values(fk_line=fk_line, fk_path=fk_path, fk_vehicle=fk_vehicle, fk_driver=fk_driver, weekday=weekday, start_time=time)
    execute_query(insert_stmt_ride)

def generate_ride(how_many):
    for _ in range(how_many):
        add_ride(fake.random_int(1, 13), fake.random_int(1, 200), fake.random_int(1, 160), fake.random_int(1, 50), fake.random_int(1, 7), fake.date_time_this_year())
if __name__ == '__main__':
    generate_ride(int(sys.argv[1]))