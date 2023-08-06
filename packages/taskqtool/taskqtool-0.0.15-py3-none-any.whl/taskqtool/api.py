import requests as rq


def getTasks():
    return rq.get("http://localhost:8000/task").json()


def deleteTask(pid):
    return rq.delete("http://localhost:8000/task", params={"pid": pid}).json()


def updateTask(tasks):
    return rq.put("http://localhost:8000/task", json=tasks).json()


def addTask(tasks):
    return rq.post("http://localhost:8000/task", json=tasks).json()