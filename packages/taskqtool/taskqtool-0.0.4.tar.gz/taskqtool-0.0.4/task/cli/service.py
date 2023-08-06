from argparse import ArgumentParser
from task.utils.resources import files as packageFiles
from pathlib import Path


def moveServiceFiles():
    files = list(packageFiles("task.statics").iterdir())
    systemPath = Path("/lib/systemd/system")
    for file in files:
        p = Path(file)
        suffix = p.suffix
        name = p.name
        newFile = systemPath / name
        if suffix == ".service" and not newFile.exists():
            content = p.read_text(encoding="utf-8")
            newFile.write_text(content, encoding="utf-8")


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
        moveServiceFiles()
