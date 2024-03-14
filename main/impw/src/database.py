import os

import pygame

from .log import Log
from .paths import PATH_DB


class Database:

    @staticmethod
    def save(surface: pygame.Surface, name: str):
        path = os.path.join(PATH_DB, name + ".png")
        pygame.image.save(
            surface,
            path
        )
        Log.info(f"Saved image for '{name}'")

    @staticmethod
    def load(name: str) -> pygame.Surface:
        path = os.path.join(PATH_DB, name + ".png")
        if not os.path.exists(path):
            Log.error(f"Could not load image '{name}': path does not exist: {path}")
            exit(1)
        return pygame.image.load(path)

    @staticmethod
    def exists(name: str):
        path = os.path.join(PATH_DB, name + ".png")
        return os.path.exists(path)
    
    @staticmethod
    def delete(name: str):
        path = os.path.join(PATH_DB, name + ".png")
        os.remove(path)
        Log.info(f"Deleted image for '{name}'")
