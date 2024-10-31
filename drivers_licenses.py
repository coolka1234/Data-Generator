from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
fake = Faker('pl_PL')
drivers_licenses_table = Table('drivers_licenses', metadata, autoload_with=engine)

def add_driver_license(issue_date, expiration_date):
    insert_stmt_dl = drivers_licenses_table.insert().values(issued_on=issue_date, expires_on=expiration_date)
    execute_query(insert_stmt_dl)

def generate_dl(how_many):
    for _ in range(how_many):
        add_driver_license(fake.date_of_birth(None, 8, 15), fake.date_of_birth(None, 0, 5))

if __name__ == '__main__':
    generate_dl(int(sys.argv[1]))