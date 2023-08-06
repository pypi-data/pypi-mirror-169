from argparse import ArgumentParser
from task.utils.resources import files as packageFiles

class CLICommand:
    """文件自动移动

    移动指定文件夹下的文件到当前文件夹并等待对应程序消耗文件后自动补充
    """

    @staticmethod
    def add_argments(parser: ArgumentParser):
        add = parser.add_argument
        add("--start", action="store_true", help="运行任务队列服务")
        add("--stop", action="store_true", help="终止任务队列服务")

    @staticmethod
    def run(args, parser):
        files = packageFiles("task.statics").iterdir()
        for file in files:
            print(file)
