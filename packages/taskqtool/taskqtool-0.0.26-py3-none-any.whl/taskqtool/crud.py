from typing import List, Union

from fastapi import Query
from starlette import status
from . import models
from . import schemas

from sqlalchemy.orm import Session


def getTask(db: Session, *, pid: str, skip: int, limit: int):
    db_query: Union[Query, None] = db.query(models.Task)
    #
    if pid:
        db_query = db_query.filter(models.Task.pid == pid)
    return db_query.offset(skip).limit(limit).all()


def deleteTask(db: Session, *, pid: str):
    task = db.query(models.Task).filter(models.Task.pid == pid).filter(models.Task.running == False).first()
    if task:
        db.query(models.Task).filter(models.Task.pid == pid).delete()
        db.commit()
        return {"status": "删除成功", "pid": task.pid, "code": status.HTTP_200_OK}
    return {"status": "记录不存在或正在运行", "pid": None, "code": status.HTTP_200_OK}


def updateTask(db: Session, *, tasks: List[schemas.Task]):
    response = []
    for task in tasks:
        _task = db.query(models.Task).filter(models.Task.pid == task.pid).first()
        if not _task:
            response.append(
                {"status": "记录不存在，请新建", "pid": task.pid, "code": status.HTTP_404_NOT_FOUND})
            continue
        db.query(models.Task).filter(models.Task.pid == task.pid).update(task.dict(exclude_unset=True))
        response.append(
            {"status": "update succeed", "pid": task.pid, "code": status.HTTP_200_OK})
    db.commit()
    return response


def addTask(db: Session, tasks: List[schemas.Task]):
    response = []
    for task in tasks:
        if db.query(models.Task).filter(models.Task.pid == task.pid).first():
            response.append(
                {"status": "记录已存在，请勿重复创建", "pid": task.pid,
                 "code": status.HTTP_202_ACCEPTED})
            continue
        db_ribbon = models.Task(**task.dict(exclude_unset=True))
        db.add(db_ribbon)
        response.append(
            {"status": "创建成功", "pid": task.pid, "code": status.HTTP_201_CREATED})
    db.commit()
    return response
