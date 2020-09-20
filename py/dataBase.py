import sqlite3

conn = sqlite3.connect("../db/main.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


def execute_into(text):
    cursor.execute(text)
    conn.commit()


def execute_sel(text):
    return cursor.execute(text).fetchall()

