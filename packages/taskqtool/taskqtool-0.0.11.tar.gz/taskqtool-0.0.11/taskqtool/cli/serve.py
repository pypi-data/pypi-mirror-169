from argparse import ArgumentParser

import uvicorn

from taskqtool.server import app



class CLICommand:
    """队列后台服务
    """

    @staticmethod
    def add_arguments(parser: ArgumentParser):
        add = parser.add_argument
        # add("--start", action="store_true", help="运行任务队列服务")
        # add("--stop", action="store_true", help="终止任务队列服务")
        # add("--status", action="store_true", help="任务队列服务状态")

    @staticmethod
    def run(args, parser):
        uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == '__main__':
    pass
