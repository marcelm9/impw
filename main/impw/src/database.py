import os
from hashlib import sha256

import pygame

from .log import Log
from .paths import PATH_DB

NUMS = 1000 # 1000 binary numbers with 40 digits each

class Database:

    @staticmethod
    def save(surface: pygame.Surface):
        # transform image to sequence of numbers and concatenate them with dots
        nums = []
        for x in range(surface.get_width()):
            for y in range(surface.get_height()):
                if surface.get_at((x, y)) == (0, 0, 0):
                    nums.append(0)
                elif surface.get_at((x, y)) == (255, 255, 255):
                    nums.append(1)
                else:
                    Log.error(f"error reading from surface: color {surface.get_at((x,y))}")
                    exit(1)

        if len(nums) % NUMS != 0:
            Log.error("bad value for NUMS (change in source code!)")
            exit(1)

        num_length = len(nums) // NUMS
        binary_translated_nums_in_str = [
            "".join(
                [str(x) for x in nums[i*num_length : (i+1)*num_length]] # these have to be strings for "join"
            ) for i in range(NUMS)
        ]
        binary_translated_nums_in_int = [
            int(n, base=2) for n in binary_translated_nums_in_str
        ]
        nums_string = ".".join(
            [str(n) for n in binary_translated_nums_in_int]
        )

        print(nums_string)
        print()
        encoded = sha256(nums_string.encode()).hexdigest()
        print(encoded)

        decoded = sha256(encoded).digest().decode()

        print()
        print(decoded)

        # hash these numbers with sha-256

        # save to a .txt file

    @staticmethod
    def load_image(name: str) -> pygame.Surface:
        pass

    @staticmethod
    def load_password(name: str) -> str:
        pass
