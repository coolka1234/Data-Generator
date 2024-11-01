from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
from fk_keys_hash_sets import load_set, user_fk_keys_set, save_set, licenses_fk_keys_set
fake = Faker('pl_PL')
drivers_table = Table('drivers', metadata, autoload_with=engine)

def add_driver(foreign_key_license,foreign_key_user):
    insert_stmt_ed = drivers_table.insert().values(fk_license=foreign_key_license,fk_user=foreign_key_user)
    execute_query(insert_stmt_ed)

def generate_drivers(how_many):
    load_set('user')
    load_set('licenses')
    for _ in range(how_many):
        f_key=fake.random_int(1, 1000)
        while f_key in user_fk_keys_set:
            f_key=fake.random_int(1, 1000)
        f_key_license=fake.random_int(1, 100)
        while f_key_license in licenses_fk_keys_set:
            f_key_license=fake.random_int(1, 100)
        add_driver(f_key_license,f_key)
        user_fk_keys_set.add(f_key)
        licenses_fk_keys_set.add(f_key_license)

if __name__ == '__main__':
    generate_drivers(int(sys.argv[1]))
    save_set('user')
    save_set('licenses')