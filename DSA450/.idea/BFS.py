from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
    def addEdge(self, u, v):
        self.graph[u].append(v)
    def bfs(self, s):
        q = [s]
        visited = {}
        visited[q[0]] = True

        while len(q) != 0:
            a  =q.pop(0)

            print(f"{a} -- >", end=" ")
            for i in self.graph[a]:
                if i not in visited:
                    visited[i] = True
                    q.append(i)
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


g.bfs(2)

