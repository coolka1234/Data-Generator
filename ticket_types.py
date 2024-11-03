from sqlalchemy import text
from numbers_info import num_of_ticket_types

num_of_ticket_types = 0


def load_ticket_types():
    from connect_to_db import execute_query

    sql_file_path = "ticket_types.sql"
    with open(sql_file_path, "r", encoding="utf-8") as file:
        query = file.read()
        for command in query.split(";"):
            if command.strip():
                execute_query(text(command))
