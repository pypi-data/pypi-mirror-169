from argparse import ArgumentParser
from task.server import MyService


class CLICommand:
    """队列后台服务
    """

    @staticmethod
    def add_argments(parser: ArgumentParser):
        add = parser.add_argument
        add("--start", action="store_true", help="运行任务队列服务")
        add("--stop", action="store_true", help="终止任务队列服务")
        add("--status", action="store_true", help="任务队列服务状态")

    @staticmethod
    def run(args, parser):
        service = MyService('taskq', pid_dir='/tmp')
        if args.start:
            return service.start()
        if args.stop:
            return service.stop()
        if args.status:
            if service.is_running():
                print("Service is running.")
            else:
                print("Service is not running.")


if __name__ == '__main__':
    pass
