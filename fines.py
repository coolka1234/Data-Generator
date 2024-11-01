from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
import random
from datetime import timedelta, date
from fk_keys_hash_sets import load_set, inspector_fk_keys_set, save_set, passenger_fk_keys_set
fake = Faker('pl_PL')
fines_table = Table('fines', metadata, autoload_with=engine)

def add_fine(fk_passanger, fk_inspector, amount, issue_date, status, deadline):
    insert_stmt_ed = fines_table.insert().values(fk_passenger=fk_passanger, fk_inspector=fk_inspector, amount=amount, issue_date=issue_date, status=status, deadline=deadline)
    execute_query(insert_stmt_ed)

def generate_fines(how_many, num_of_passengers, num_of_ticket_inspectors):
    load_set('passangers')
    load_set('inspectors')
    for _ in range(how_many):
        f_key_passanger=fake.random_int(1, num_of_passengers)
        while f_key_passanger in passenger_fk_keys_set:
            f_key_passanger=fake.random_int(1, num_of_passengers)
        f_key_inspector=fake.random_int(1, num_of_ticket_inspectors)
        while f_key_inspector in inspector_fk_keys_set:
            f_key_inspector=fake.random_int(1, num_of_ticket_inspectors)
        issue_date = fake.date_time_between(date(year=2023, month=1, day=1), date(year=2023, month=12, day=31))
        deadline = issue_date + timedelta(days=random.randint(1, 365))
        add_fine(f_key_passanger, f_key_inspector, fake.random_int(1, 500), issue_date, fake.random_int(0, 1), deadline)

if __name__ == '__main__':
    generate_fines(int(sys.argv[1]))
    save_set('passangers')
    save_set('inspectors')