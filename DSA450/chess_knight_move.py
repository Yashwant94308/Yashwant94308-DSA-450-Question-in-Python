import numpy as np
import sys
sys.setrecursionlimit(100000)

count = 0


def knightTour(chess, i, j, n):
    global count
    if i < 1 or j < 1 or i >= len(chess) or j >= len(chess):
        return
    if n == 0:
        if chess[i][j] == 0:
            count += 1
            chess[i][j] += 1

        return
    else:
        knightTour(chess, i - 2, j + 1, n - 1)
        knightTour(chess, i - 1, j + 2, n - 1)
        knightTour(chess, i + 1, j + 2, n - 1)
        knightTour(chess, i + 2, j + 1, n - 1)
        knightTour(chess, i + 2, j - 1, n - 1)
        knightTour(chess, i + 1, j - 2, n - 1)
        knightTour(chess, i - 1, j - 2, n - 1)
        knightTour(chess, i - 2, j - 1, n - 1)


if __name__ == '__main__':
    chesss = np.zeros((10, 10))

    x, y, N = (int(i) for i in input().split())
    knightTour(chesss, x, y, N)
    print(count)
