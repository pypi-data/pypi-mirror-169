from service import Service
from os import system
from taskqtool.utils.resources import files as packageFiles
from pathlib import Path

class MyService(Service):
    def run(self):
        files = packageFiles("taskqtool").iterdir()
        for file in files:
            p = Path(file)
            print(p)
            print(p.stem)
            if p.stem == "myService":
                system(f"uvicorn server:app --app-dir {p.parent.__str__()}")
