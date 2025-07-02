from fastapi import FastAPI
import database
import os

app = FastAPI()

#if not os.path.isfile("database.sqlite"):
#    database.initdb()
#    createvalues()

#def createvalues():
#    database.query("INSERT INTO ninja VALUES (1, 1, 'Alice', NULL, 0), (2, 0, 'Bob', NULL, 0), (3, 1, 'Charlie', NULL, 1), (4, 0, 'Mateus', 3, 0)")
#    database.query("INSERT INTO task VALUES ('fios'), ('cham-cham'), ('copos')")

@app.get("/registar_impostor")
def registar_impostor(ninja: int):
    return database.query('UPDATE ninja SET impostor=1 WHERE id=?', (impostor,))

@app.get("/matar_ninja")
def matar_ninja(impostor: int, ninja: int):
    if database.query('SELECT impostor FROM ninja WHERE id=?', (impostor,)):
        database.query('UPDATE ninja SET killed_by=? WHERE id=?', (impostor, ninja))
        database.query('UPDATE ninja SET cooldown=1 WHERE id=?', (impostor,))
        return {"impostor": impostor, "ninja": ninja}
    else:
        return {"erro": "não é impostor"}

@app.get("/completar_task")
def completar_task(task: str, ninja: int):
    if database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,)):
        database.query('UPDATE ninja SET cooldown=0 WHERE id=?', (ninja,))
        return {"impostor": ninja}
    else:
        database.query('INSERT INTO completed_task (ninja_id, task) VALUES (?, ?)', (ninja, task))
        return {"task": task, "ninja": ninja}

@app.get("/emergency_meeting_start")
def emergency_meeting_start(type: str, ninja: int):
    return {"type": type, "ninja": ninja}

@app.get("/emergency_meeting_end")
def emergency_meeting_end():
    return {"end": "ok"}

@app.get("/log")
def log(index: int):
    return {"log": log[index:]}

@app.get("/info")
def info():
    return {"ninjas": [{"id": 0, "nome": "Bob", "impostor": True, "cooldown": False, "killed_by": 1, "tasks_completed": []}], "tasks": {"completed": 5, "total": 30}}

@app.get("/emergency_meeting_on")
def emergency_meeting_on() -> bool:
    return bool(database.query("SELECT active FROM emeeting")[0][0])