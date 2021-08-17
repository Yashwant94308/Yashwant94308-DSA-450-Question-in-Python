graph = [[0, 4, 6, 0, 0, 0],
         [4, 0, 6, 3, 4, 0],
         [6, 6, 0, 1, 0, 0],
         [0, 3, 1, 0, 2, 3],
         [0, 4, 0, 2, 0, 7],
         [0, 0, 0, 3, 7, 0], ]
n = 6


def select_min_val(distance, sm):
    m = float('inf')
    ver = None
    for i in range(n):
        if not sm[i] and distance[i] < m:
            ver = i
            m = distance[i]
    return ver


parent = [0] * n
parent[0] = -1
dis = [float('inf')] * n
dis[0] = 0
set_mst = [False] * n
# set_mst[0] = True

for i in range(n):
    u = select_min_val(dis, set_mst)
    # print(u)
    if u is None:
        break
    set_mst[u] = True
    for j in range(n):
        if graph[u][j] != 0 and not set_mst[j] and graph[u][j] < dis[j]:
            dis[j] = graph[u][j]
            parent[j] = u
for i in range(n):
    print('U-->V', parent[i], '-->', i, ' wt = ', graph[parent[i]][i])
