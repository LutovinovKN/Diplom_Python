from flask import Flask, render_template
import sqlite3
import os

if "mydb.db" not in os.listdir():
    conn = sqlite3.connect("mydb.db")
    db = conn.cursor()
    
    db.execute("CREATE TABLE posts (title TEXT, content TEXT, \
        date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP)")
    conn.commit()
    conn.close()

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/posts")
def display_posts():
    return render_template("posts.html",)

if __name__ == "__main__":
    app.run(debug=True)

