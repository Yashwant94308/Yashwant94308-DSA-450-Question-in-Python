from collections import defaultdict

n = 9
p = 6
a = [7, 5, 4, 2, 9, 3]
b = [4, 9, 6, 8, 7, 1]
d = [98, 72, 10, 22, 17, 66]

graph = defaultdict(list)


def addEdge(graph, u, v, wt):
    graph[u].append([v, wt])


edge = []
for i in range(len(a)):
    edge.append([a[i], b[i], d[i]])
edge.sort(key=lambda x: x[0])

for i in range(len(edge)):
    addEdge(graph, edge[i][0], edge[i][1], edge[i][2])

vis = []
ans = []
print(graph)
for node in graph:
    while True:
        if node in graph and node not in vis:
            vis.append(node)
            ans.append([node, graph[node][0][0], graph[node][0][1]])
            node = graph[node][0][0]
        else:
            break

print(ans)
