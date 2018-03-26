# coding=utf-8
import pygame
from astar import a_star
import heuristic

__author__ = 'Agustin Castillo'


# Cambiar aquí para activar una u otra función heurística.

# h = heuristic.default
h = heuristic.manhattan_distance
# h = heuristic.max_difference
# h = heuristic.min_difference
# h = heuristic.avg_difference


##########################################################################################

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (128, 128, 255)

pygame.init()

size = [255, 255]
window = pygame.display.set_mode(size)
pygame.display.set_caption("A*")

playing = True
clock = pygame.time.Clock()

grid_dimension = 10
grid_width = 20
grid_height = 20
grid_margin = 5

# The board is represented by a grid of characters where 1 is floor and 0 is an obstacle
grid = [['1' for x in range(grid_dimension)] for y in range(grid_dimension)]
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
            column = pos[1] // (grid_width + grid_margin)
            row = pos[0] // (grid_height + grid_margin)
            if event.button == 1:
                # left click
                if grid[row][column] != '1':
                    grid[row][column] = '1'
                else:
                    grid[row][column] = '0'
            elif event.button == 3:
                # right click
                grid[row][column] = '1'
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
    for i in range(grid_dimension):
        for j in range(grid_dimension):
            color = WHITE
            if grid[i][j] == '0':
                color = RED
            elif ((i, j) in path) or ((i, j) == start) or ((i, j) == end):
                color = GREEN
            elif any(n.x == j and n.y == i for n in nodes):
                color = BLUE
            pygame.draw.rect(window, color,
                             [(grid_margin + grid_width) * i + grid_margin,
                              (grid_margin + grid_height) * j + grid_margin,
                              grid_width,
                              grid_height])
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
