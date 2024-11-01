from connect_to_db import  engine 



def load_ticket_types():
    sql_file_path = "ticket_types.sql"
    with open(sql_file_path, 'r') as file:
        sql_commands = file.read()

    with engine.connect() as connection:
        connection.execute(sql_commands)