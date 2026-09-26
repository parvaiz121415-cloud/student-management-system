from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


def create_database():
    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER,
            course TEXT
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():

    student_id = request.form["id"]
    name = request.form["name"]
    age = request.form["age"]
    course = request.form["course"]

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute(
        "INSERT INTO students VALUES (?, ?, ?, ?)",
        (student_id, name, age, course)
    )

    connection.commit()
    connection.close()

    return redirect("/")


@app.route("/delete/<int:student_id>")
def delete_student(student_id):

    connection = sqlite3.connect("students.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )

    connection.commit()
    connection.close()

    return redirect("/")


if __name__ == "__main__":

    create_database()

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)