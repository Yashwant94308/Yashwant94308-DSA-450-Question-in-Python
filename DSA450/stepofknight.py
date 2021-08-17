res = [1e9]
N = 101
KnightPos = [101, 101]
TargetPos = [1, 1]
vis = [[0 for j in range(N + 1)] for i in range(N + 1)]


dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

def bfs():
    q = [[KnightPos[0], KnightPos[1], 0]]
    vis[KnightPos[0]][KnightPos[1]] = 1
    while len(q) > 0:
        t = q.pop(0)
        if t[0] == TargetPos[0] and t[1] == TargetPos[1]:
            return t[2]
        for i in range(8):
            x = t[0] + dx[i]
            y = t[1] + dy[i]
            if 1 <= x <= N and 1 <= y <= N and vis[x][y] == 0:
                vis[x][y] = 1
                q.append([x,y,t[2]+1])
print(bfs())






# def dfs(r, c, vis, step):
#     if r > N or r < 1 or c > N or c < 1 or vis[r][c] != 0:
#         # print('h')
#         return
#     if r == TargetPos[0] and c == TargetPos[1]:
#         print(res)
#         res[0] = min(res[0], step)
#         return
#     vis[r][c] = -1
#     dfs(r + 2, c + 1, vis, step + 1)
#     dfs(r + 2, c - 1, vis, step + 1)
#     dfs(r - 2, c + 1, vis, step + 1)
#     dfs(r - 2, c - 1, vis, step + 1)
#     dfs(r + 1, c + 2, vis, step + 1)
#     dfs(r + 1, c - 2, vis, step + 1)
#     dfs(r - 1, c + 2, vis, step + 1)
#     dfs(r - 1, c - 2, vis, step + 1)
#     vis[r][c] = 0
#
#
# dfs(KnightPos[0], KnightPos[1], vis, 0)
# print(res[0])
