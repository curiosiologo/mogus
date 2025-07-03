from fastapi import FastAPI
import database
import os

app = FastAPI()

# Este valor muda quando dados sobre os ninjas forem atualizados.
# Assim, o cliente só atualiza quando for necessário.
ninja_counter = 0

def createvalues():
    database.query("INSERT INTO ninja VALUES (0, 0, 'Alice', NULL, 0), (1, 0, 'Bob', NULL, 0), (2, 1, 'Charlie', NULL, 1), (3, 0, 'Mateus', 2, 0)")
    database.query("INSERT INTO task VALUES ('fios'), ('cham-cham'), ('copos')")
    database.query("INSERT INTO log VALUES (0, 'Boas'), (2, 'segunda'), (1, 'primeira')")
    print("creating values")

if database.created:
    createvalues()

@app.get("/registar_impostor")
def registar_impostor(ninja: int):
    database.query('UPDATE ninja SET impostor=1 WHERE id=?', (ninja,))
    return {"registar_impostor": "ok"}

@app.get("/matar_ninja")
def matar_ninja(impostor: int, ninja: int):
    global ninja_counter

    if not database.query('SELECT impostor FROM ninja WHERE id=?', (impostor,))[0][0]:
        return {"erro": "não é impostor"}
    if database.query('SELECT cooldown FROM ninja WHERE id=?', (impostor,))[0][0]:
        return {"erro": "on cooldown"}
    if database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,))[0][0]:
        return {"erro": "não podes matar impostores"}
    if database.query('SELECT killed_by FROM ninja WHERE id=?', (ninja,))[0][0]:
        return {"erro": "ninja já morto"}
    if database.query('SELECT killed_by FROM ninja WHERE id=?', (impostor,))[0][0]: # FIXME já morto... ejetado?
        return {"erro": "impostor já morto"}
    database.query('UPDATE ninja SET killed_by=? WHERE id=?', (impostor, ninja))
    database.query('UPDATE ninja SET cooldown=1 WHERE id=?', (impostor,))
    ninja_counter += 1
    return {"impostor": impostor, "ninja": ninja}

@app.get("/completar_task")
def completar_task(task: str, ninja: int):
    global ninja_counter

    if database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,))[0][0]:
        database.query('UPDATE ninja SET cooldown=0 WHERE id=?', (ninja,))
        print(database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,)))[0][0]
        ninja_counter += 1
        return {"impostor": ninja}
    elif not database.query('SELECT killed_by FROM ninja WHERE id=?', (ninja,))[0][0]:
        database.query('INSERT INTO completed_task (ninja_id, task) VALUES (?, ?)', (ninja, task))
        ninja_counter += 1
        return {"task": task, "ninja": ninja}
    else:
        return {"erro": "ninja morto"}

@app.get("/emergency_meeting_start")
def emergency_meeting_start(report: bool, ninja: int):
    database.query("UPDATE emeeting SET active=1,report=?,reporter=?", (1 if report else 0, ninja))

@app.get("/emergency_meeting_end")
def emergency_meeting_end():
    database.query("UPDATE emeeting SET active=0")

@app.get("/emergency_meeting_on")
def emergency_meeting_on() -> bool:
    return bool(database.query("SELECT active FROM emeeting")[0][0])

@app.get("/log")
def log():
    return database.query("SELECT * FROM log ORDER BY id")
    
@app.get("/latest_msg")
def latest_msg():
    return log()[0]

@app.get("/task_progress")
def task_progress():
    completed = int(database.query("SELECT COUNT(1) FROM completed_task")[0][0])
    TOTAL = 50
    return (completed / TOTAL) * 100
    
@app.get("/info")
def info():
    return {
        "ninjas": database.query("SELECT * FROM ninja"),
        "ninja_counter": ninja_counter,
        "task_progress": task_progress(),
        "emeeting": database.query("SELECT * FROM emeeting")[0],
        "reactor": database.query("SELECT * FROM reactor")[0]
    }