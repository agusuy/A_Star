# coding=utf-8
__author__ = 'Agustin Castillo'


class Node:
    def __init__(self, x, y, parent=None, cost=float("inf")):
        self.x = x
        self.y = y
        self.parent = parent
        self.cost = cost

    def get_tuple(self):
        return self.y, self.x

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "(%s,%s)" % (self.x, self.y)


def cost_default(grid, start, goal):
    return 1


def heuristic_default(start, goal):
    return 0


def a_star(start_xy, goal_xy, grid, cost=cost_default, heuristic=heuristic_default):
    """
    Finds a path from start to goal using the A* algorithm
    :param start_xy: tuple (x,y)
    :param goal_xy: tuple (x,y)
    :param grid:
    :param cost: cost function
    :param heuristic: heuristic function
    :return: the list of nodes in the path and a list of explored nodes
    """
    start = Node(start_xy[1], start_xy[0], cost=0)
    goal = Node(goal_xy[1], goal_xy[0])

    reachable = [start]  # or frontier, nodes that can be reach from the start
    explored = []  # nodes already explored

    while reachable:
        node = choose(reachable, heuristic, goal)

        if node == goal:
            # finish!
            path = reconstruct_path(node)
            return path, explored

        reachable.remove(node)
        explored.append(node)

        adjacent = get_adjacent(grid, node.x, node.y)
        new_reachable = [item for item in adjacent if item not in explored]

        for adjacent in new_reachable:
            if adjacent not in reachable:
                reachable.append(adjacent)

            if node.cost + 1 < adjacent.cost:
                adjacent.parent = node
                adjacent.cost = node.cost + 1

    return [], explored


def get_adjacent(grid, x, y):

    return [Node(j, i)
            for i in range(y - 1, y + 2) if 0 <= i < len(grid)
            for j in range(x - 1, x + 2) if 0 <= j < len(grid[0])
            if (i != y) != (j != x) and grid[i][j] != '0']


def choose(reachable, heuristic, goal):
    min_cost = float('inf')
    best = None

    for node in reachable:
        g = node.cost
        f = heuristic(node, goal)
        cost = g + f

        if min_cost > cost:
            min_cost = cost
            best = node

    return best


def reconstruct_path(n):
    path = []
    while n is not None:
        ij = n.get_tuple()
        path.append(ij)
        n = n.parent
        path.reverse()
    return path
