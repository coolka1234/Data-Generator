from connect_to_db import execute_query, engine, metadata
from sqlalchemy import Table, insert
from faker import Faker
import sys

fake = Faker("pl_PL")
rides_table = Table("rides", metadata, autoload_with=engine)
weekdays = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
]


def add_ride(fk_line, fk_path, fk_vehicle, fk_driver, weekday, time):
    insert_stmt_ride = rides_table.insert().values(
        fk_line=fk_line,
        fk_path=fk_path,
        fk_vehicle=fk_vehicle,
        fk_driver=fk_driver,
        weekday=weekday,
        start_time=time,
    )
    execute_query(insert_stmt_ride)


def generate_ride(
    how_many, num_of_lines, num_of_paths, num_of_vehicles, num_of_drivers
):
    for _ in range(how_many):
        add_ride(
            fake.random_int(1, num_of_lines),
            fake.random_int(1, num_of_paths),
            fake.random_int(1, num_of_vehicles),
            fake.random_int(1, num_of_drivers),
            fake.random_element(elements=weekdays),
            fake.date_time_this_year(),
        )


if __name__ == "__main__":
    generate_ride(int(sys.argv[1]))
