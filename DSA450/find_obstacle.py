arr = [[1, 0, 0],
       [1, 0, 0],
       [1, 9, 1]]


def spm(grid):
    m = len(grid)
    n = len(grid[0])

    q = [[0, 0, 0]]
    grid[0][0] = 0

    dire = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while len(q) != 0:

        points = q.pop(0)

        if grid[points[0]][points[1]] == 9:
            return points[2]

        for d in dire:
            r = points[0] + d[0]
            c = points[1] + d[1]
            if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                q.append([r, c, points[2] + 1])
                grid[r][c] = 1
            elif grid[r][c] == 9:
                return points[2] + 1

    return -1


print(spm(arr))
