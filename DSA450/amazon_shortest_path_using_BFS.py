grids = [['0', '*', '0', 's'],
         ['*', '0', '*', '*'],
         ['0', '*', '*', '*'],
         ['d', '*', '*', '*']]
R = len(grids)
C = len(grids[0])

vis = [[False for i in range(len(grids[0]) + 1)] for j in range(len(grids) + 1)]
st = -1
end = -1
for i in range(R):
    for j in range(C):
        if grids[i][j] == '0':
            vis[i][j] = True
        if grids[i][j] == 's':
            st = i
            end = j
cnt = 0
q = [[st, end, cnt]]
# print(q)
f = True
vis[st][end] = True
# print(vis)
while len(q) > 0:
    points = q.pop(0)

    if grids[points[0]][points[1]] == 'd':
        print(points[2])
        f = False
        break

    if points[0] - 1 >= 0 and vis[points[0] - 1][points[1]] == False:
        q.append([points[0] - 1, points[1], points[2] + 1])
        vis[points[0] - 1][points[1]] = True

    if points[0] + 1 < R and not vis[points[0] + 1][points[1]]:
        q.append([points[0] + 1, points[1], points[2] + 1])
        vis[points[0] + 1][points[1]] = True

    if points[1] - 1 >= 0 and vis[points[0]][points[1] - 1] == False:
        q.append([points[0], points[1] - 1, points[2] + 1])
        vis[points[1] - 1][points[1]] = True

    if points[1] + 1 < C and vis[points[0]][points[1] + 1] == False:
        q.append([points[0], points[1] + 1, points[2] + 1])
        vis[points[1] + 1][points[1]] = True

if f:
    print(-1)
