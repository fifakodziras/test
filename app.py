import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    db = sqlite3.connect('users.db')
    db.row_factory = sqlite3.Row
    c = db.cursor()
    c.execute("SELECT * FROM history")
    rows = c.fetchall()
    return render_template("index.html", identy=rows)

if __name__ == "__main__":
    app.run(debug=True)