from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table 
from faker import Faker
import sys
fake = Faker('pl_PL')
purchases_table = Table('purchases', metadata, autoload_with=engine)

def add_purchase(date, amount):
    insert_stmt_purchase = purchases_table.insert().values(date=date, amount=amount)
    execute_query(insert_stmt_purchase)

def generate_purchases(how_many):
    for _ in range(how_many):
        #add december!
        add_purchase(fake.date_time_this_year(), abs(fake.pyfloat(2, 2))+1.0)

if __name__ == '__main__':
    generate_purchases(int(sys.argv[1]))
