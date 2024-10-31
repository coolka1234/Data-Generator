from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
from fk_keys_hash_sets import load_set, user_fk_keys_set, save_set
fake = Faker('pl_PL')
passengers_table = Table('passengers', metadata, autoload_with=engine)

def add_passenger(foreign_key_user):
    insert_stmt_passenger = passengers_table.insert().values(fk_user=foreign_key_user)
    execute_query(insert_stmt_passenger)

def generate_passengers(how_many):
    load_set('user')
    for _ in range(how_many):
        f_key=fake.random_int(1, 1000)
        while f_key in user_fk_keys_set:
            f_key=fake.random_int(1, 1000)
        add_passenger(f_key)
        user_fk_keys_set.add(f_key)

if __name__ == '__main__':
    generate_passengers(int(sys.argv[1]))
    save_set('user')