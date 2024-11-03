from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys
import random
from fk_keys_hash_sets import save_set, load_set, vehicles_numbers_set

fake = Faker("pl_PL")
vehicles_table = Table("vehicles", metadata, autoload_with=engine)

vehicle_types = ["Bus", "Tram"]
vehicle_statuses = ["Active", "Inactive"]


def add_vehicle(
    vehicle_number,
    last_service_date,
    production_date,
    capacity,
    type,
    status,
    air_conditioning,
):
    insert_stmt_vehicle = vehicles_table.insert().values(
        vehicle_number=vehicle_number,
        last_technical_inspection=last_service_date,
        production_date=production_date,
        capacity=capacity,
        type=type,
        status=status,
        air_conditioning=air_conditioning,
    )
    execute_query(insert_stmt_vehicle)


def generate_vehicles(how_many):
    load_set("vehicles")
    for _ in range(how_many):
        vehicle_number = fake.random_int(1000, 9999)
        while vehicle_number in vehicles_numbers_set:
            vehicle_number = fake.random_int(1000, 9999)
        add_vehicle(
            vehicle_number,
            fake.date_time_this_decade(0, 5),
            fake.date_time_this_decade(8, 15),
            fake.random_int(min=1, max=100),
            fake.random_element(elements=vehicle_types),
            fake.random_element(elements=vehicle_statuses),
            fake.random_element(elements=(True, False)),
        )
        vehicles_numbers_set.add(vehicle_number)


if __name__ == "__main__":
    generate_vehicles(int(sys.argv[1]))
    save_set("vehicles")
