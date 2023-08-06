from argparse import ArgumentParser
from pprint import pprint

from ..api import deleteTask


class CLICommand:
    """显示所有队列
    """

    @staticmethod
    def add_arguments(parser: ArgumentParser):
        add = parser.add_argument
        add("--pid", help="删除任务的pid")

    @staticmethod
    def run(args, parser):
        res = deleteTask(args.pid)
        pprint(res)


if __name__ == '__main__':
    pass
