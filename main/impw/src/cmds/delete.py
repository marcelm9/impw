import os

from ..log import Log
from ..database import Database

ARGS_LEN = 1

def delete(args: list[str]):
    if len(args) != ARGS_LEN:
        Log.error("invalid args")
        exit(1)

    if not Database.exists(args[0]):
        Log.error(f"No image found for name '{args[0]}'")
        exit(1)

    if Log.input(f"Are you sure you want to delete the image for '{args[0]}'? (y/n) ") == "y":
        Database.delete(args[0])
    else:
        Log.info("Cancelled")
