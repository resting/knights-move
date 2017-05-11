import sys
import numpy as np
import getnextmoves as gnm


def setUnreachable(grid, start):
    # Iterate through grid, set 0 to -1 if is it not = to starting point
    for yidx, r in enumerate(grid):
        for xidx, n in enumerate(r):
            if (n == 0 and not any(np.equal([xidx, yidx], [start]).all(1))):
                grid[yidx][xidx] = -1


def main():
    x, y, x0, y0 = [int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])]

    grid = [[0] * x for i in range(y)]
    bounds = [x - 1, y - 1]

    seen = []
    q = []

    start = np.array([x0, y0])
    q.append(start)

    c = 0
    while q:
        v = q.pop(0)
        seen.append(v)
        c += 1

        nextMoves = gnm.getNextMoves(v, bounds)

        for directions in nextMoves:
            for nextMove in directions:
                if len(nextMove) != 0 and not any(np.equal(nextMove, seen).all(1)):
                    if len(q) != 0 and not any(np.equal(nextMove, q).all(1)):
                        grid[nextMove[1]][nextMove[0]] = grid[v[1]][v[0]] + 1
                        q.append(nextMove)
                    elif (len(q) == 0):
                        grid[nextMove[1]][nextMove[0]] = grid[v[1]][v[0]] + 1
                        q.append(nextMove)

    setUnreachable(grid, start)

    for r in grid:
        print (''.join([str(n).rjust(3, ' ') for n in r]))


if __name__ == '__main__':
    main()
