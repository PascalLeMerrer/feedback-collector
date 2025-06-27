import json
import db

connection = db.connect()
cursor = connection.cursor()

cursor.execute("DROP TABLE IF EXISTS sessions;")
cursor.execute(
    """
                CREATE TABLE sessions(id int NOT NULL PRIMARY KEY,
                title VARCHAR(150) NOT NULL,
                starts_at TIMESTAMP WITH TIME ZONE NOT NULL,
                ends_at TIMESTAMP WITH TIME ZONE NOT NULL)
                """
)


def escape(string):
    return string.replace("'", " ")


with open("www/data/all.json") as file:
    data = json.load(file)
    sessions = data[0]["sessions"]
    for session in sessions:
        title = escape(session["title"])
        cursor.execute(
            f"""
            INSERT INTO sessions(id, title, starts_at, ends_at)
            VALUES('{session["id"]}', '{title}', '{session["startsAt"]}', '{session["endsAt"]}')
            """
        )

connection.commit()

cursor.close()
connection.close()
