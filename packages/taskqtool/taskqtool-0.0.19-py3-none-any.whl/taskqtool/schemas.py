from typing import Union
from pydantic import BaseModel


class Task(BaseModel):
    pid: str
    startTime: Union[int, None] = None
    submitTime: Union[int, None] = None
    running: Union[bool, None] = None
    scriptPath: Union[str, None] = None
    shell: Union[str, None] = None


class TaskDelete(BaseModel):
    pid: int
