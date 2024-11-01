from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table
from faker import Faker
import sys
fake = Faker('pl_PL')
technical_issues_table = Table('technical_issues', metadata, autoload_with=engine)

def add_ti(description, report_date, resolve_date, fk_driver, fk_vehicle, status, repair_cost):
    insert_stmt_ti = technical_issues_table.insert().values(description=description, report_date=report_date, resolve_date=resolve_date, fk_driver=fk_driver, fk_vehicle=fk_vehicle, status=status, repair_cost=repair_cost)
    execute_query(insert_stmt_ti)

def generate_ti(how_many):
    for _ in range(how_many):
        add_ti(fake.text(), fake.date_time_this_year(), fake.date_time_this_year(), fake.random_int(1, 50), fake.random_int(1, 160), fake.random_elements(elements=('Completed', 'In progress', 'Reported')), fake.pyfloat(10, 2, positive=True, min_value=100, max_value=10000))

if __name__ == '__main__':
    generate_ti(int(sys.argv[1]))