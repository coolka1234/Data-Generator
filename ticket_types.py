from connect_to_db import  engine 
from numbers_info import num_of_ticket_types


def load_ticket_types():
    sql_file_path = "ticket_types.sql"
    with open(sql_file_path, 'r') as file:
        sql_commands = file.read()
        num_of_ticket_types = sql_commands.count('INSERT INTO')

    with engine.connect() as connection:
        connection.execute(sql_commands)