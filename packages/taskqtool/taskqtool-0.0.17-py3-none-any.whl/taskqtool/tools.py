
import subprocess
from subprocess import Popen



class Pipe:
    def __init__(self, command, current_directory, encoding="utf-8"):
        self.command = command
        self.current_directory = current_directory
        self.encoding = encoding
        self.stdout = ""
        self.stderr = ""
        self.pipe()

    def pipe(self):
        popen = Popen(self.command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True,
                      cwd=self.current_directory)
        stdout, stderr = popen.communicate()
        if stdout:
            self.stdout = stdout.decode(self.encoding)
            return
        if stderr:
            self.stderr = stderr.decode(self.encoding)

