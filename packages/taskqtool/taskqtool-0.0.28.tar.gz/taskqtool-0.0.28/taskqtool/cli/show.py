from argparse import ArgumentParser
from pprint import pprint
import time
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
        startTime = res["startTime"]
        submitTime = res["submitTime"]
        if startTime:
            res["startTime"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(startTime))
        if submitTime:
            res["submitTime"] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(submitTime))
        pprint(res)



if __name__ == '__main__':
    pass
