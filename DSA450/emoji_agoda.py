grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]


def islandPerimeter(grid):
    R = len(grid)
    C = len(grid[0])

    res = [0]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == 1:
                if i - 1 < 0 or grid[i - 1][j] == 0:
                    res[0] += 1
                if i + 1 >= R or grid[i + 1][j] == 0:
                    res[0] += 1
                if j - 1 < 0 or grid[i][j - 1] == 0:
                    res[0] += 1
                if j + 1 >= C or grid[i][j + 1] == 0:
                    res[0] += 1
    return res[0]


print(islandPerimeter(grid))
