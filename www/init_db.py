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
cursor.execute("""CREATE TABLE sessions(id int NOT NULL PRIMARY KEY,
                                        title VARCHAR(150) NOT NULL,
                                        starts_at TIMESTAMP WITH TIME ZONE NOT NULL,
                                        ends_at TIMESTAMP WITH TIME ZONE NOT NULL) """)



connection.commit()

cursor.close()
connection.close()