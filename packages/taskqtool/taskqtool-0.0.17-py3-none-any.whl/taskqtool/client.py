import time
from pathlib import Path
from taskqtool.api import getTasks, deleteTask, updateTask
from taskqtool.tools import Pipe


def consumer():
    while True:
        tasks = getTasks()
        if len(tasks) > 0:
            task = tasks.pop(0)
            path = Path(task["scriptPath"])
            task["running"] = True
            updateTask([task])
            pipe = Pipe(command=f'{task["shell"]} {path.__str__()}', current_directory=path.parent, encoding="utf-8")
            if pipe.stdout:
                with open(path.parent / "task.out", "a+") as fd:
                    fd.write(pipe.stdout)
            if pipe.stderr:
                with open(path.parent / "task.err", "a+") as fd:
                    fd.write(pipe.stderr)
            deleteTask(task["pid"])
            time.sleep(1)
        else:
            time.sleep(2)


if __name__ == '__main__':
    consumer()
