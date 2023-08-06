from argparse import ArgumentParser
from pprint import pprint

from ..api import getTasks


class CLICommand:
    """显示所有队列
    """

    @staticmethod
    def add_arguments(parser: ArgumentParser):
        pass

    @staticmethod
    def run(args, parser):
        res = getTasks()
        pprint(res)



if __name__ == '__main__':
    pass
