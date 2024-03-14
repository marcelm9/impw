import os

from ..log import Log
from ..paths import PATH_DB

ARGS_LEN = 0

def list_(args: list[str]):
    if len(args) != ARGS_LEN:
        Log.error("invalid args")
        exit(1)

    files = [f.removesuffix(".png") for f in os.listdir(PATH_DB) if not f.startswith("__")]

    if len(files) == 0:
        Log.info("No saves")
        return

    Log.info("Saves:")
    for filename in files:
        Log.info(f" - {filename}")
