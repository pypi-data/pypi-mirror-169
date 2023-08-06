import json
import time
from argparse import ArgumentParser
from pathlib import Path
from pprint import pprint

from ..api import addTask
import uuid


class CLICommand:
    """提交队列
    """

    @staticmethod
    def add_arguments(parser: ArgumentParser):
        add = parser.add_argument
        add("--scriptPath", default="./sub.sh", help="队列服务运行路径")
        add("--shell", default="bash", help="队列脚本shell[bash,sh,python,...]")

    @staticmethod
    def run(args, parser):
        scriptPath = Path(args.scriptPath).absolute()
        shell = args.shell
        submitTime = time.time()
        pid = uuid.uuid1(clock_seq=int(submitTime))
        running = False
        print(json.dumps({
            "scriptPath": scriptPath.__str__(),
            "shell": shell,
            "submitTime": submitTime,
            "pid": pid.hex,
            "running": running
        }))
        res = addTask([{
            "scriptPath": scriptPath.__str__(),
            "shell": shell,
            "submitTime": submitTime,
            "pid": pid.int,
            "running": running
        }])
        pprint(res)


if __name__ == '__main__':
    pass
