from fastapi import FastAPI
import psycopg2
import json

app = FastAPI()

# PostgreSQL-ге қосылу функциясы
def get_connection():
    return psycopg2.connect(
        host="db",
        database="mydb",
        user="myuser",
        password="mypassword"
    )

# Қолданба іске қосылғанда кесте құру
def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100)
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

init_db()


@app.get("/")
def root():
    return {"message": "Hello from Docker!"}


@app.get("/users")
def get_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM users;")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    users = [{"id": r[0], "name": r[1]} for r in rows]
    return users
