from ..log import Log

ARGS_LEN = 1

def edit(args: list[str]):
    if len(args) != ARGS_LEN:
        Log.error("invalid args")
