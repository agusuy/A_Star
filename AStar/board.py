# coding=utf-8
import pygame
from astar import a_star
import heuristic
from constants import WINDOW_SIZE, TILE_DIMENSION, GRID_WIDTH, GRID_HEIGHT, TILE_MARGIN, WINDOW_TITLE, FPS, \
    BLACK, WHITE, GREEN, RED, BLUE, FLOOR, OBSTACLE

__author__ = 'Agustin Castillo'


# Cambiar aquí para activar una u otra función heurística.

# h = heuristic.default
h = heuristic.manhattan_distance
# h = heuristic.max_difference
# h = heuristic.min_difference
# h = heuristic.avg_difference


##########################################################################################

pygame.init()

window = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption(WINDOW_TITLE)

playing = True
clock = pygame.time.Clock()

# The board is represented by a grid of characters where 1 is floor and 0 is an obstacle
grid = [[FLOOR for x in range(TILE_DIMENSION)] for y in range(TILE_DIMENSION)]
path = []
nodes = []
start = None
end = None

while playing:
    # user events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[1] // (GRID_WIDTH + TILE_MARGIN)
            row = pos[0] // (GRID_HEIGHT + TILE_MARGIN)
            if event.button == 1:
                # left click
                if grid[row][column] != FLOOR:
                    grid[row][column] = FLOOR
                else:
                    grid[row][column] = OBSTACLE
            elif event.button == 3:
                # right click
                grid[row][column] = FLOOR
                pos = (row, column)
                if start is None:
                    start = pos
                elif end is None:
                    end = pos
                else:
                    start = pos
                    end = None

    # Logic
    if start and end:
        path, nodes = a_star(start, end, grid, heuristic=h)

    # Draw
    window.fill(BLACK)
    for i in range(TILE_DIMENSION):
        for j in range(TILE_DIMENSION):
            color = WHITE
            if grid[i][j] == OBSTACLE:
                color = RED
            elif ((i, j) in path) or ((i, j) == start) or ((i, j) == end):
                color = GREEN
            elif any(n.x == j and n.y == i for n in nodes):
                color = BLUE
            pygame.draw.rect(window, color,
                             [(TILE_MARGIN + GRID_WIDTH) * i + TILE_MARGIN,
                              (TILE_MARGIN + GRID_HEIGHT) * j + TILE_MARGIN,
                              GRID_WIDTH,
                              GRID_HEIGHT])
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
