import os
import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="postgres",
    user=os.environ['DB_USERNAME'],
    password=os.environ['DB_PASSWORD']
)

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS sessions;')

connection.commit()

cursor.close()
connection.close()