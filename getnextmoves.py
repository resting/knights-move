import numpy as np

def inBounds(u, bounds):
    return True if (u[0] <= bounds[0] and u[1] <= bounds[1]) else False


def move(v, m1, m2, bounds):
    rs = []
    a = v + m1
    if (min(a) >= 0 and inBounds(a, bounds)):
        rs.append(a)
    a = v + m2
    if (min(a) >= 0 and inBounds(a, bounds)):
        rs.append(a)
    return rs


def getNextMoves(v, bounds):
    top = move(v, np.array([-1, -2]), np.array([1, -2]), bounds)
    bottom = move(v, np.array([-1, 2]), np.array([1, 2]), bounds)
    left = move(v, np.array([-2, -1]), np.array([-2, 1]), bounds)
    right = move(v, np.array([2, -1]), np.array([2, 1]), bounds)

    return [top, bottom, left, right]