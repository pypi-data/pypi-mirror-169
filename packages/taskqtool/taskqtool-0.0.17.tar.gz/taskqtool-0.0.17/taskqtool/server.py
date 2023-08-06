import json
from typing import List

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from . import crud
from taskqtool.database import SessionLocal
from taskqtool.schemas import Task, TaskDelete

app = FastAPI(
    title="队列系统",
    contact={
        "name": "Zhao Hao",
        "email": "601095001@qq.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post(path="/task")
def addTask(tasks: List[Task], db: Session = Depends(get_db)):
    return crud.addTask(db, tasks)


@app.delete(path="/task")
def deleteTask(pid: int, db: Session = Depends(get_db)):
    return crud.deleteTask(db, pid=pid)


@app.get(path="/task")
def getTask(pid: int=None, skip: int=0, limit: int=1000, db: Session = Depends(get_db)):
    return crud.getTask(db, pid=pid, skip=skip, limit=limit)


@app.put(path="/task")
def updateTask(tasks: List[Task], db: Session = Depends(get_db)):
    return crud.updateTask(db, tasks=tasks)


if __name__ == '__main__':
    uvicorn.run("server:app", host="0.0.0.0", port=8000)
