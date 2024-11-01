from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
from fk_keys_hash_sets import load_set, save_set, path_fk_keys_set, line_numbers_set
fake = Faker('pl_PL')
lines_table = Table('lines', metadata, autoload_with=engine)

def add_line(number, fk_main_path, avg_frequency):
    insert_stmt_line = lines_table.insert().values(number=number, fk_main_path=fk_main_path, avg_frequency=avg_frequency)
    execute_query(insert_stmt_line)

def generate_line(how_many):
    load_set('paths')
    load_set('line_numbers')
    for _ in range(how_many):
        f_key=fake.random_int(1, 100)
        number=fake.random_int(1, 50)
        while number in line_numbers_set:
            number=fake.random_int(1, 50)
        while f_key in path_fk_keys_set:
            f_key=fake.random_int(1, 100)
        add_line(fake.random_int(1, 50), f_key, fake.random_int(1, 90))
        path_fk_keys_set.add(f_key)
        line_numbers_set.add(number)

if __name__ == '__main__':
    generate_line(int(sys.argv[1]))
    save_set('paths')
    save_set('line_numbers')
