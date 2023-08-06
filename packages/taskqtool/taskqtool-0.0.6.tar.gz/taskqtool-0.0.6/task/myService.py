from service import Service
from os import system
from task.utils.resources import files as packageFiles
from pathlib import Path

class MyService(Service):
    def run(self):
        files = packageFiles("task").iterdir()
        for file in files:
            p = Path(file)
            if p.stem == "myService":
                system(f"uvicorn server:app --app-dir {p.parent.__str__()}")
