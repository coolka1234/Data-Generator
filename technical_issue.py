from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table
from faker import Faker
import sys
from datetime import date, timedelta
import random
fake = Faker('pl_PL')
technical_issues_table = Table('technical_issues', metadata, autoload_with=engine)

def add_ti(description, report_date, resolve_date, fk_driver, fk_vehicle, status, repair_cost):
    insert_stmt_ti = technical_issues_table.insert().values(description=description, report_date=report_date, resolve_date=resolve_date, fk_driver=fk_driver, fk_vehicle=fk_vehicle, status=status, repair_cost=repair_cost)
    execute_query(insert_stmt_ti)

def generate_ti(how_many):
    for _ in range(how_many):
        report_date = fake.date_time_between(date(year=2023, month=1, day=1), date(year=2023, month=12, day=31))
        if(random.randint(0, 1) == 0):
            resolve_date = None
        else:
            resolve_date = report_date + timedelta(days=random.randint(1, 365))
        add_ti(fake.text(), report_date, resolve_date, fake.random_int(1, 50), fake.random_int(1, 160), fake.random_elements(elements=('Completed', 'In progress', 'Reported')), fake.pyfloat(10, 2, positive=True, min_value=100, max_value=10000))

if __name__ == '__main__':
    generate_ti(int(sys.argv[1]))