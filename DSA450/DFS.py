from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def dfs(self, s, visited):

        visited.add(s)
        print(f"{s}  -->", end=" ")

        for i in self.graph[s]:
            if i not in visited:
                self.dfs(i, visited)


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 9)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
vis = set()
g.dfs(2, vis)
