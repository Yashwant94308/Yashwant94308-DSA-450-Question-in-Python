matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
R = len(matrix)
C = len(matrix[0])
res = []
vis = [[False for i in range(C + 1)] for j in range(R + 1)]


def dfs(row, col):
    if col < 0 or col >= C:
        return
    if row < 0 or row >= R:
        return
    if vis[row][col]:
        return
    res.append(matrix[row][col])
    print(res)
    for i, j in zip(range(row + 1), range(col + 1)):
        # print(i, j)
        if vis[i][j]:
            break

        # print(res)

        dfs(i, j + 1)
        dfs(i + 1, j)
        dfs(i, j - 1)
        dfs(i - 1, j)


dfs(R - 1, C - 1)
print(res)
