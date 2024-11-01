from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table
from faker import Faker
import sys
fake = Faker('pl_PL')
tickets_table = Table('tickets', metadata, autoload_with=engine)

def add_tickets(fk_passanger, fk_purchase, fk_ticket_type):
    insert_stmt_tickets = tickets_table.insert().values(fk_passenger=fk_passanger, fk_purchase=fk_purchase, fk_ticket_type=fk_ticket_type)
    execute_query(insert_stmt_tickets)

def generate_tickets(how_many):
    for _ in range(how_many):
        add_tickets(fake.random_int(1, 100), fake.random_int(1, 10000), fake.random_int(1, 20))


if __name__ == '__main__':
    generate_tickets(int(sys.argv[1]))