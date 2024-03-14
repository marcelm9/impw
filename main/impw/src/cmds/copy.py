from ..log import Log
from ..database import Database
from ..crypto_manager import CryptoManager
import pyperclip

ARGS_LEN = 1

def copy(args: list[str]):
    if len(args) != ARGS_LEN:
        Log.error("invalid args")
        exit(1)

    if not Database.exists(args[0]):
        Log.error(f"No image found for name '{args[0]}'")
        exit(1)

    pyperclip.copy(
        CryptoManager.image_to_hash(
            Database.load(
                args[0]
            )
        )
    )
    Log.info(f"Copied password for '{args[0]}' to clipboard")
