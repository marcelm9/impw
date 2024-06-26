from rich import print

class Log:

    @staticmethod
    def info(msg: str):
        print(f"\[[purple]impw[/]]\[[green]info[/]] {msg}")

    @staticmethod
    def warn(msg: str):
        print(f"\[[purple]impw[/]]\[[yellow]warn[/]] {msg}")

    @staticmethod
    def error(msg: str):
        print(f"\[[purple]impw[/]]\[[red]error[/]] {msg}")

    @staticmethod
    def input(msg: str):
        print(f"\[[purple]impw[/]]\[[cyan]input[/]] {msg}", end="")
        return input()
