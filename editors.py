from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
from fk_keys_hash_sets import load_set, user_fk_keys_set, save_set
fake = Faker('pl_PL')
editors_table = Table('editors', metadata, autoload_with=engine)

def add_editor(foreign_key_user):
    insert_stmt_ed = editors_table.insert().values(fk_user=foreign_key_user)
    execute_query(insert_stmt_ed)

def generate_editors(how_many, num_of_app_users):
    load_set('user')
    for _ in range(how_many):
        f_key=fake.random_int(1, num_of_app_users)
        while f_key in user_fk_keys_set:
            f_key=fake.random_int(1, num_of_app_users)
        add_editor(f_key)
        user_fk_keys_set.add(f_key)

if __name__ == '__main__':
    generate_editors(int(sys.argv[1]))
    save_set('user')