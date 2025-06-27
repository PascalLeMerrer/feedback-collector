from flask import Flask
from flask import render_template
from . import db

app = Flask(__name__)


@app.route("/")
def home():

    connection = db.connect()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM sessions;")
    sessions = cursor.fetchall()
    cursor.close()
    connection.close()
    print(sessions)
    return render_template("hello.html")


if __name__ == "__main__":
    app.run(debug=True)
