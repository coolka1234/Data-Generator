from connect_to_db import  engine 
from numbers_info import num_of_ticket_types
from sqlalchemy import text


def load_ticket_types():
    sql_file_path = "ticket_types.sql"
    with open(sql_file_path, 'r') as file:
        sql_commands = file.read()
        num_of_ticket_types = sql_commands.count('INSERT INTO')
    command=sql_commands.strip().split(';')

    with engine.connect() as connection:
        for command in command:
            if command.strip():
                connection.execute(text(command))
        connection.commit()