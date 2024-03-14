import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import argparse

from impw.src.log import Log

from impw.src.cmds import *


parser = argparse.ArgumentParser()
parser.add_argument("command")
parser.add_argument("args", nargs="*", default=[])
parsed_args = parser.parse_args()

command = parsed_args.command
args = parsed_args.args

match command:
    case "help":
        print("ipmw - Password manager using images")
        print("Available commands:")
        for c in "copy.delete.list.new.show".split("."):
            print(f" - {c}")
    case "copy":
        copy(args)
    case "delete":
        delete(args)
    case "list":
        list_(args)
    case "new":
        new(args)
    case "show":
        show(args)
    case _:
        Log.error("unknown command")
        exit(1)
