arr = [[3, 3, 1, 0],
       [3, 0, 3, 3],
       [2, 3, 0, 3],
       [0, 3, 3, 3]]
st = []
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            st = [i, j]
res = [1e9]


def dfs(road, row, col, cnt):
    if row >= len(arr) or col >= len(arr[0]) or row < 0 or col < 0:
        return
    if road[row][col] == 0:
        return

    if road[row][col] == 2:
        res[0] = min(res[0], cnt)
        return
    temp = road[row][col]
    road[row][col] = 0
    dfs(road, row + 1, col, cnt + 1)
    dfs(road, row - 1, col, cnt + 1)
    dfs(road, row, col + 1, cnt + 1)
    dfs(road, row, col - 1, cnt + 1)
    road[row][col] = temp


dfs(arr, st[0], st[1], 0)
print(res)
