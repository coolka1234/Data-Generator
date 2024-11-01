from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
fake = Faker('pl_PL')
stops_table = Table('stops', metadata, autoload_with=engine)

def add_stop(name, type, longitude, latitude, seating_available, shelter):
    insert_stmt_inspection = stops_table.insert().values(name=name, type=type, longitude=longitude, latitude=latitude, seating_available=seating_available, shelter=shelter)
    execute_query(insert_stmt_inspection)

def generate_stops(how_many):
    set_ad=set()
    address=fake.street_address()
    while address in set_ad:
        address=fake.street_address()+fake.random_element(elements=('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'))
    for _ in range(how_many):
        add_stop(fake.street_address(), fake.random_element(elements=('bus', 'tram')), fake.longitude(), fake.latitude(), fake.random_element(elements=(True, False)), fake.random_element(elements=(True, False)))

if __name__ == '__main__':
    generate_stops(int(sys.argv[1]))