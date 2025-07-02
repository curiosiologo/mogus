import sqlite3

database = sqlite3.connect("database.sqlite")

def script(script: str):
    cursor = database.cursor()
    cursor.executescript(script)
    
script("PRAGMA foreign_keys = 1;")

def query(query: str, params: tuple[object] = []) -> list[tuple[object]] | None:
    try:
        cursor = database.cursor()
        cursor.execute(query, params)
        return cur.fetchall()
    except sqlite3.Error as e:
        print(f"ERROR: Could not run query '{query}' because '{e.sqlite_errorname}'")
        return None

def initdb():
    with open('initdb.sql', 'r') as file:
        content = file.read()
        script(content)