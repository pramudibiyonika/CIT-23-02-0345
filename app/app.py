from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="rootpassword",
        database="taskdb"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    conn = get_db_connection()
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            title VARCHAR(100),
            done BOOLEAN DEFAULT FALSE
        )
    """)

    if request.method == "POST":
        title = request.form.get("title")
        if title:
            cursor.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
            conn.commit()

    cursor.execute("SELECT id, title, done FROM tasks")
    tasks = cursor.fetchall()

    conn.close()
    return render_template("index.html", tasks=tasks)

@app.route("/done/<int:task_id>")
def mark_done(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET done=TRUE WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=%s", (task_id,))
    conn.commit()
    conn.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

