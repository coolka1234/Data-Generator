from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
from fk_keys_hash_sets import load_set, inspector_fk_keys_set, save_set, passenger_fk_keys_set
fake = Faker('pl_PL')
fines_table = Table('fines', metadata, autoload_with=engine)

def add_fine(fk_passanger, fk_inspector, amount, issue_date, status, deadline):
    insert_stmt_ed = fines_table.insert().values(fk_passenger=fk_passanger, fk_inspector=fk_inspector, amount=amount, issue_date=issue_date, status=status, deadline=deadline)
    execute_query(insert_stmt_ed)
# DATES DONT WORK ARE INCORRECT
def generate_fines(how_many):
    load_set('passangers')
    load_set('inspectors')
    for _ in range(how_many):
        f_key_passanger=fake.random_int(1, 100)
        while f_key_passanger in passenger_fk_keys_set:
            f_key_passanger=fake.random_int(1, 100)
        f_key_inspector=fake.random_int(1, 100)
        while f_key_inspector in inspector_fk_keys_set:
            f_key_inspector=fake.random_int(1, 100)
        add_fine(f_key_passanger, f_key_inspector, fake.random_int(1, 500), fake.date_time_this_decade(1500, 800), fake.random_int(0, 1), fake.date_time_this_century(0, 700))

if __name__ == '__main__':
    generate_fines(int(sys.argv[1]))
    save_set('passangers')
    save_set('inspectors')