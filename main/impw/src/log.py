from rich import print

class Log:

    @staticmethod
    def info(msg: str):
        print(f"\[[purple]impw[/]]\[[green]info[/]] {msg}")

    @staticmethod
    def warn(msg: str):
        print(f"\[[purple]impw[/]]\[[yellow]info[/]] {msg}")

    @staticmethod
    def error(msg: str):
        print(f"\[[purple]impw[/]]\[[red]info[/]] {msg}")
