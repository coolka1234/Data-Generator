from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table
from faker import Faker
import sys
from fk_keys_hash_sets import load_set, path_stops_fk_keys_set, save_set
fake = Faker('pl_PL')
path_stops_table = Table('path_stops', metadata, autoload_with=engine)

def add_path_stops(id_path, id_stop, path_minute):
    insert_stmt_ps = path_stops_table.insert().values(id_path=id_path, id_stop=id_stop, path_minute=path_minute)
    execute_query(insert_stmt_ps)

def generate_path_stops(how_many, num_of_paths, num_of_lines):
    load_set('path_stops')
    for _ in range(how_many):
        while True:
            id_path = fake.random_int(1, num_of_paths)
            id_stop = fake.random_int(1, num_of_lines)
            path_minute = fake.random_int(1, 1000)
            if f'{id_path}-{id_stop}' not in path_stops_fk_keys_set:
                path_stops_fk_keys_set.add(f'{id_path}-{id_stop}')
                add_path_stops(id_path, id_stop, path_minute)
                break


if __name__ == '__main__':
    generate_path_stops(int(sys.argv[1]))
    save_set('path_stops')