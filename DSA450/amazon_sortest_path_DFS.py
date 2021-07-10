grids = [['0', '*', '0', 's'],
         ['*', '0', '*', '*'],
         ['0', '*', '*', '*'],
         ['d', '*', '*', '*']]
R = len(grids)
C = len(grids[0])

# vis = [[False for i in range(len(grid[0]))] for j in range(len(grid))]
res = [1e9]


def dfs(grid, row, col, cnt):
    if row < 0 or row >= R:
        return
    if col < 0 or col >= C:
        return
    if grid[row][col] == '0':
        return
    if grid[row][col] == 'd':
        res[0] = min(res[0], cnt)
        return
    temp = grid[row][col]
    grid[row][col] = '0'
    dfs(grid, row + 1, col, cnt + 1)
    dfs(grid, row - 1, col, cnt + 1)
    dfs(grid, row, col + 1, cnt + 1)
    dfs(grid, row, col - 1, cnt + 1)
    grid[row][col] = temp
st = -1
end = -1
for i in range(R):
    for j in range(C):
        if grids[i][j] == 's':
            st = i
            end = j
            break
dfs(grids, st, end, 0)
print(res[0])
