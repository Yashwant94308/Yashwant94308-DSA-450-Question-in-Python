N = 4
M = 6
mat = ([[10, 10, 2, 0, 20, 4],
        [1, 0, 0, 30, 2, 5],
        [0, 10, 4, 0, 2, 0],
        [1, 0, 2, 20, 0, 4]])


def sol():
    res = -1
    for i in range(M):
        res = max(res, mat[0][i])
    for i in range(1, N):
        res = -1
        for j in range(M):
            if 0 < j < M - 1:
                mat[i][j] += max(mat[i - 1][j], max(mat[i - 1][j + 1], mat[i - 1][j - 1]))
            elif j > 0:
                mat[i][j] += max(mat[i - 1][j], mat[i - 1][j - 1])
            elif j < M - 1:
                mat[i][j] += max(mat[i - 1][j], mat[i - 1][j + 1])
            res = max(mat[i][j], res)
    return res


print(sol())
