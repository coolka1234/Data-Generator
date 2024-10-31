from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import os
import sys
fake = Faker('pl_PL')
user_table = Table('app_users', metadata, autoload_with=engine)

def add_user(login, password, email, phone_number, name, surname):
    insert_stmt_user = user_table.insert().values(login=login, password=password, email=email, phone_number=phone_number, name=name, surname=surname)
    execute_query(insert_stmt_user)

def generate_users(how_many):
    for _ in range(how_many):
        add_user(fake.user_name(), fake.password(), fake.email(), fake.phone_number(), fake.first_name(), fake.last_name())

if __name__ == '__main__':
    generate_users(int(sys.argv[1]))