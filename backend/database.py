import sqlite3
import os

database = sqlite3.connect(
    "database.sqlite",
    check_same_thread = False) # FIXME: Será que isto causa problemas...??

def script(script: str):
    cursor = database.cursor()
    cursor.executescript(script)
    
script("PRAGMA foreign_keys = 1;")

# FIXME: Isto não devia retornar um dicionário??
def query(query: str, params: tuple[object] = []) -> list[tuple[object]] | None:
    try:
        cursor = database.cursor()
        cursor.execute(query, params)
        database.commit()
        return cursor.fetchall()
    except sqlite3.Error as e:
        print(f"ERROR: Could not run query '{query}' because '{str(e)}'")
        return None

def initdb():
    with open('initdb.sql', 'r') as file:
        content = file.read()
        script(content)