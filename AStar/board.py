import pygame

import heuristic
from astar import a_star
from constants import GRID_DIMENSION, TILE_WIDTH, TILE_HEIGHT, TILE_MARGIN, \
    BLACK, WHITE, GREEN, RED, BLUE, FLOOR, OBSTACLE


class Board:

    def __init__(self):
        # The board is represented by a grid of characters where 1 is floor and 0 is an obstacle
        self.grid = [[FLOOR for x in range(GRID_DIMENSION)] for y in range(GRID_DIMENSION)]

    def draw(self, window, start, end, path, nodes):
        window.fill(BLACK)
        for i in range(GRID_DIMENSION):
            for j in range(GRID_DIMENSION):
                color = WHITE
                if self.grid[i][j] == OBSTACLE:
                    color = RED
                elif ((i, j) in path) or ((i, j) == start) or ((i, j) == end):
                    color = GREEN
                elif any(n.x == j and n.y == i for n in nodes):
                    color = BLUE
                pygame.draw.rect(window, color,
                                 [(TILE_MARGIN + TILE_WIDTH) * i + TILE_MARGIN,
                                  (TILE_MARGIN + TILE_HEIGHT) * j + TILE_MARGIN,
                                  TILE_WIDTH,
                                  TILE_HEIGHT])

    def path(self, start, end):

        # h = heuristic.default
        h = heuristic.manhattan_distance
        # h = heuristic.max_difference
        # h = heuristic.min_difference
        # h = heuristic.avg_difference

        return a_star(start, end, self.grid, heuristic=h)
