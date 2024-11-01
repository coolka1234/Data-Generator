from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
import random
fake = Faker('pl_PL')
user_table = Table('app_users', metadata, autoload_with=engine)

def add_user(login, password, email, phone_number, name, surname):
    insert_stmt_user = user_table.insert().values(login=login, password=password, email=email, phone_number=phone_number, name=name, surname=surname)
    execute_query(insert_stmt_user)

def generate_users(how_many):
    for _ in range(how_many):
        random.seed()
        email=fake.email()
        username=fake.user_name()
        random_number = random.randint(0, 100000) # can be improved
        random_string=fake.random_element(elements=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'))+str(random_number)
        email=fake.email()
        email=email.split('@')[0]+random_string+'@'+email.split('@')[1]
        random_number = random.randint(0, 100000)
        username=fake.user_name()+str(random_number)+fake.random_element(elements=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'))
        add_user( username,fake.password(), email, fake.phone_number(), fake.first_name(), fake.last_name())

if __name__ == '__main__':
    generate_users(int(sys.argv[1]))
