import pygame

from ..log import Log
from ..config import *
from ..database import Database

ARGS_LEN = 1

def show(args: list[str]):
    if len(args) != ARGS_LEN:
        Log.error("invalid args")
        exit(1)

    if not Database.exists(args[0]):
        Log.error(f"No image found for name {args[0]}")
        exit(1)


    screen = pygame.display.set_mode((SIDELENGTH * PIXEL_SIZE, SIDELENGTH * PIXEL_SIZE))
    fpsclock = pygame.time.Clock()
    fps = 60
    pygame.display.set_caption(f"impw - {args[0]}")

    img = Database.load(args[0])
    img = pygame.transform.scale(img, (SIDELENGTH * PIXEL_SIZE, SIDELENGTH * PIXEL_SIZE))
    screen.blit(img, (0,0))

    run = True
    while run:
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.display.flip()
        fpsclock.tick(fps)
