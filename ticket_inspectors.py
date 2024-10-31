from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
from fk_keys_hash_sets import load_set, user_fk_keys_set, save_set
fake = Faker('pl_PL')
ticket_inspectors_table = Table('ticket_inspectors', metadata, autoload_with=engine)

def add_ticket_inspector(foreign_key_user):
    insert_stmt_ti = ticket_inspectors_table.insert().values(fk_user=foreign_key_user)
    execute_query(insert_stmt_ti)

def generate_ticket_inspectors(how_many):
    load_set('user')
    for _ in range(how_many):
        f_key=fake.random_int(1, 1000)
        while f_key in user_fk_keys_set:
            f_key=fake.random_int(1, 1000)
        add_ticket_inspector(f_key)
        user_fk_keys_set.add(f_key)

if __name__ == '__main__':
    generate_ticket_inspectors(int(sys.argv[1]))
    save_set('user')