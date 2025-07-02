from fastapi import FastAPI

app = FastAPI()

@app.get("/registar_impostor")
def matar_ninja(ninja: int):
    return {"ninjas": ninja}

@app.get("/matar_ninja")
def matar_ninja(impostor: int, ninja: int):
    return {"impostor": impostor, "ninja": ninja}

@app.get("/completar_task")
def completar_task(task: str, ninja: int):
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

def emergency_meeting_on():
    return {"emergency_meeting_on": False}