import os
import psycopg2


def connect():
    connection = psycopg2.connect(
        host="localhost",
        database="postgres",
        user=os.environ["DB_USERNAME"],
        password=os.environ["DB_PASSWORD"],
    )
    return connection
