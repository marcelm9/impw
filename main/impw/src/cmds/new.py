import pygame

from ..log import Log
from ..database import Database

SIDELENGTH = 200
PIXEL_SIZE = 3

ARGS_LEN = 1

def new(args: list[str]):
    if len(args) != ARGS_LEN:
        Log.error("invalid args")
        exit(1)

    if Database.exists(args[0]):
        Log.error(f"Image for name '{args[0]}' already exists")
        exit(1)
    
    screen = pygame.display.set_mode((SIDELENGTH * PIXEL_SIZE, SIDELENGTH * PIXEL_SIZE))
    surface = pygame.Surface((SIDELENGTH, SIDELENGTH))
    fpsclock = pygame.time.Clock()
    fps = 120

    old_pos = None

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
                elif event.key == pygame.K_r:
                    surface.fill((0,0,0))

        if pygame.mouse.get_pressed()[0] or pygame.mouse.get_pressed()[2]:
            color = (255,255,255) if pygame.mouse.get_pressed()[0] else (0,0,0)
            pos = pygame.mouse.get_pos()
            pos = pos[0] // PIXEL_SIZE, pos[1] // PIXEL_SIZE
            if old_pos is not None:
                pygame.draw.line(
                    surface,
                    color,
                    old_pos,
                    pos,
                    1
                )
            else:
                surface.set_at(
                    pos,
                    color
                )
            old_pos = pos
        else:
            old_pos = None

        pygame.transform.scale(surface, (SIDELENGTH * PIXEL_SIZE, SIDELENGTH * PIXEL_SIZE), screen)
        pygame.display.flip()
        fpsclock.tick(fps)

    Database.save(surface, args[0])
