# coding=utf-8
__author__ = 'Agustin Castillo'


def default(n, f):
    """ Retorna siempre cero. Hecha para poder correr el algoritmo A* sin tener
        heuristicas definidas.
    """
    return 0

def manhattan_distance(n, f):
    """ Retorna la distancia de Manhattan entre los nodos n y f. Esto es la suma
        de las diferencias entre las coordenadas correspondientes.
    """
    dx = abs(n.x - f.x)
    dy = abs(n.y - f.y)
    return dx + dy


def max_difference(n, f):
    """ Retorna la maxima de las diferencias entre las coordenadas
        correspondientes de los nodos n y f.
    """
    dx = abs(n.x - f.x)
    dy = abs(n.y - f.y)
    return max(dx, dy)


def min_difference(n, f):
    """ Retorna la minima de las diferencias entre las coordenadas
        correspondientes de los nodos n y f.
    """
    dx = abs(n.x - f.x)
    dy = abs(n.y - f.y)
    return min(dx, dy)


def avg_difference(n, f):
    """ Retorna la promedio de las diferencias entre las coordenadas
        correspondientes de los nodos n y f.
    """
    dx = abs(n.x - f.x)
    dy = abs(n.y - f.y)
    return (dx + dy) / 2.0
