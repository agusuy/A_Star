import pygame

from constants import WINDOW_SIZE, TILE_WIDTH, TILE_HEIGHT, TILE_MARGIN, WINDOW_TITLE, FPS, \
    FLOOR, OBSTACLE
from board import Board


class Game:

    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(WINDOW_SIZE)
        pygame.display.set_caption(WINDOW_TITLE)

    def loop(self):
        playing = True
        clock = pygame.time.Clock()

        maze = Board()

        start = None
        end = None

        while playing:
            # User events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    playing = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    column = pos[1] // (TILE_WIDTH + TILE_MARGIN)
                    row = pos[0] // (TILE_HEIGHT + TILE_MARGIN)
                    if event.button == 1:
                        # left click
                        if maze.grid[row][column] != FLOOR:
                            maze.grid[row][column] = FLOOR
                        else:
                            maze.grid[row][column] = OBSTACLE
                    elif event.button == 3:
                        # right click
                        maze.grid[row][column] = FLOOR
                        pos = (row, column)
                        if start is None:
                            start = pos
                        elif end is None:
                            end = pos
                        else:
                            start = pos
                            end = None

            # Logic
            path = []
            nodes = []
            if start and end:
                path, nodes = maze.path(start, end)

            # Draw
            maze.draw(self.window, start, end, path, nodes)

            pygame.display.flip()
            clock.tick(FPS)

        pygame.quit()
