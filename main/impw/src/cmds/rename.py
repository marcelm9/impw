from ..log import Log
from ..database import Database

ARGS_LEN = 2

def rename(args: list[str]):
    if len(args) != ARGS_LEN:
        Log.error("invalid args")
        exit(1)

    if not Database.exists(args[0]):
        Log.error(f"Could not find image for name '{args[0]}'")
        exit(1)

    if Database.exists(args[1]):
        Log.error(f"Image for name '{args[1]}' already exists")
        exit(1)

    Database.rename(args[0], args[1])
