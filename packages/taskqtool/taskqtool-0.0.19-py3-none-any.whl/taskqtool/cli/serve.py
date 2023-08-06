from argparse import ArgumentParser


class CLICommand:
    """队列后台服务
    """

    @staticmethod
    def add_arguments(parser: ArgumentParser):
        add = parser.add_argument
        add("--server", action="store_true", help="运行任务队列服务")
        add("--client", action="store_true", help="终止任务队列客户端")
        # add("--status", action="store_true", help="任务队列服务状态")

    @staticmethod
    def run(args, parser):
        if args.server:
            import uvicorn
            from taskqtool.server import app
            return uvicorn.run(app, host="0.0.0.0", port=8000)
        if args.client:
            from taskqtool.client import consumer
            return consumer()


if __name__ == '__main__':
    pass
