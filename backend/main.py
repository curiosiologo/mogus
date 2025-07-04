from fastapi import FastAPI
import database
import time
import threading

app = FastAPI()

# Este valor muda quando dados sobre os ninjas forem atualizados.
# Assim, o cliente só atualiza quando for necessário.
ninja_counter = 0

INITIAL_REACTOR_COUNTDOWN = 30
reactor_countdown = INITIAL_REACTOR_COUNTDOWN
meltdown_thread: threading.Thread = None

def createvalues():
    database.query("INSERT INTO ninja VALUES (0, 0, 'Alice', NULL, 0), (1, 0, 'Bob', NULL, 0), (2, 1, 'Charlie', NULL, 1), (3, 0, 'Mateus', 2, 0), (4, 0, 'Wilber', NULL, 0)")
    database.query("INSERT INTO log VALUES (0, 'Boas'), (2, 'segunda'), (1, 'primeira')")
    print("creating values")

if database.created:
    createvalues()

TASKLIST = database.query("SELECT name FROM task")
TOTAL = database.query("SELECT COUNT(id) FROM ninja")[0][0] * len(TASKLIST)

@app.get("/registar_impostor")
def registar_impostor(ninja: int):
    database.query('UPDATE ninja SET impostor=1 WHERE id=?', (ninja,))
    return {"status": "ok"}

@app.get("/matar_ninja")
def matar_ninja(impostor: int, ninja: int):
    global ninja_counter

    if not database.query('SELECT impostor FROM ninja WHERE id=?', (impostor,))[0][0]:
        return {"status": "Não é impostor"}
    if database.query('SELECT cooldown FROM ninja WHERE id=?', (impostor,))[0][0]:
        return {"status": "On cooldown"}
    print(database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,))[0][0])
    if database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,))[0][0]:
        return {"status": "Impostores não podem matar impostores"}
    if database.query('SELECT killed_by FROM ninja WHERE id=?', (ninja,))[0][0]:
        return {"status": "Ninja já morto"}
    if database.query('SELECT killed_by FROM ninja WHERE id=?', (impostor,))[0][0]: # FIXME já morto... ejetado?
        return {"status": "Impostor já morto"}
    database.query('UPDATE ninja SET killed_by=? WHERE id=?', (impostor, ninja))
    database.query('UPDATE ninja SET cooldown=1 WHERE id=?', (impostor,))
    ninja_counter += 1
    return {"status": "ok", "impostor": impostor, "ninja": ninja}

@app.get("/ninjas_vivos")
def ninjas_vivos():
    return {"status": "ok", "ninjas": database.query("SELECT * FROM ninja WHERE killed_by=NULL")}

@app.get("/completar_task")
def completar_task(task: str, ninja: int):
    global ninja_counter

    if database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,))[0][0]:
        database.query('UPDATE ninja SET cooldown=0 WHERE id=?', (ninja,))
        print(database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,))[0][0])
        ninja_counter += 1
        return {"status": "ok", "impostor": ninja}
    elif not database.query('SELECT killed_by FROM ninja WHERE id=?', (ninja,))[0][0]:
        database.query('INSERT INTO completed_task (ninja_id, task) VALUES (?, ?)', (ninja, task))
        ninja_counter += 1
        return {"status": "ok", "task": task, "ninja": ninja}
    else:
        return {"status": "Ninja morto"}

@app.get("/emergency_meeting_start")
def emergency_meeting_start(report: bool, ninja: int):
    database.query("UPDATE emeeting SET active=1,report=?,reporter=?", (1 if report else 0, ninja))
    return {"status": "ok"}

@app.get("/emergency_meeting_end")
def emergency_meeting_end():
    database.query("UPDATE emeeting SET active=0")
    return {"status": "ok"}

"""@app.get("/emergency_meeting_on")
def emergency_meeting_on():
    return {"status": "ok", "value": bool(database.query("SELECT active FROM emeeting")[0][0])}"""

@app.get("/log")
def log():
    return {"status": "ok", "log": database.query("SELECT * FROM log ORDER BY id")}

@app.get("/create_msg")
def create_msg(message: str):
    latest_id = len(log()["log"])
    database.query("INSERT INTO log VALUES (?, ?)", (latest_id+1, message))
    return {"status": "ok", "log": (latest_id+1, message)}

@app.get("/set_stairs")
def set_stairs(stair: str, state: bool):
    database.query("UPDATE stairs SET active=? WHERE location=?", (1 if state else 0, stair))
    return {"status": "ok"}

@app.get("/get_stairs")
def get_stairs():
    stairs = database.query("SELECT * FROM stairs")
    return {"status": "ok", "stairs": stairs}

"""@app.get("/activate_reactor")
def activate_reactor(ninja: int):
    if not database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,))[0][0]:
        return {"status": "Não é impostor"}
    if database.query('SELECT active FROM reactor')[0][0]:
        return {"status": "Reactor já ativado"}
    database.query("UPDATE reactor SET active=1, ninja=?", (ninja,))
    return {"status": "ok"}

@app.get("/deactivate_reactor")
def deactivate_reactor():
    if database.query('SELECT active FROM reactor')[0][0]:
        return {"status": "Reactor já deativado"}
    database.query("UPDATE reactor SET active=0, ninja=?", (None,))
    return {"status": "ok"}"""

@app.get("/reactor_state")
def reactor_state():
    state = database.query('SELECT * FROM reactor')
    return {"status": "ok", "state": state}

@app.get("/latest_msg")
def latest_msg():
    return {"status": "ok", "log": log()["log"][-1]}

def task_progress():
    completed = int(database.query("SELECT COUNT(1) FROM completed_task")[0][0])
    return (completed / TOTAL) * 100
    
@app.get("/tasks")
def get_tasks():
    return {"status": "ok", "tasks": database.query("SELECT * FROM task")}
    
@app.get("/set_meltdown")
def set_meltdown(ninja: int | None = None):
    global reactor_countdown
    
    if ninja != None and not database.query('SELECT impostor FROM ninja WHERE id=?', (ninja,))[0][0]:
        return {"status": "Crewmates não podem ativar o estado do reator"}
    
    database.query("UPDATE reactor SET active=?", (1 if ninja != None else 0,))
    if ninja != None:
        database.query("UPDATE reactor SET activator=?", (ninja,))
        meltdown_thread.start()
    else:
        reactor_countdown = INITIAL_REACTOR_COUNTDOWN
        
    return {"status": "ok"}

def meltdown_on():
    return bool(database.query("SELECT active FROM reactor")[0][0])

@app.get("/info")
def info():
    out = {
        "status": "ok",
        "ninjas": database.query("SELECT * FROM ninja"),
        "ninja_tasks": dict(database.query("SELECT ninja_id, (COUNT(*) / ?) * 100 FROM completed_task GROUP BY ninja_id", (float(len(TASKLIST)),))),
        "ninja_counter": ninja_counter,
        "task_progress": task_progress(),
        "emeeting": database.query("SELECT * FROM emeeting")[0],
        "stairs": get_stairs(),
        "reactor": database.query("SELECT * FROM reactor")[0],
    }
    return out
    
def reactor_countdown_run():
    global reactor_countdown
    
    cancelled = False
    
    while reactor_countdown >= 0:
        if not reactor_state()["state"][0][0]:
            cancelled = True
            break
    
        time.sleep(1)
        print("countdown: " + str(reactor_countdown))
        reactor_countdown -= 1
        
    if not cancelled:
        # TODO: Os impostores ganham??
        print("BOOM!!!!!! Impostores ganham, supostamente.")
        pass
        
meltdown_thread = threading.Thread(target=reactor_countdown_run)