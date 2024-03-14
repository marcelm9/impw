from hashlib import sha256

import pygame

from .log import Log

NUMS = 1000 # 1000 binary numbers with 40 digits each

class CryptoManager:

    def image_to_hash(surface: pygame.Surface) -> str:
        # transform image to sequence of numbers and concatenate them with dots
        s = ""
        for x in range(surface.get_width()):
            for y in range(surface.get_height()):
                if surface.get_at((x, y)) == (0, 0, 0):
                    s += "0"
                elif surface.get_at((x, y)) == (255, 255, 255):
                    s += "1"
                else:
                    Log.error(f"error reading from surface: color {surface.get_at((x,y))}")
                    exit(1)

        return sha256(s.encode()).hexdigest()
