from collections import defaultdict


class Graph:
    def __init__(self, Edges):
        self.Edges = Edges
        self.dict = {}
        # d = defaultdict(self.Edges)
        # print("d", d)
        for start, end in self.Edges:
            if start not in self.dict:
                self.dict[start] = [end]
            else:
                self.dict[start].append(end)
        print(self.dict)

    def AllPath(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.dict:
            return []
        paths = []
        for node in self.dict[start]:
            if node not in path:
                new_path = self.AllPath(node, end, path)

                for i in new_path:
                    paths.append(i)
        return paths

    def SortestPath(self, start, end, path=[]):

        path = path + [start]
        if start == end:
            return path
        if start not in self.dict:
            return None
        spaths = None
        for node in self.dict[start]:
            if node not in path:
                sp = self.SortestPath(node, end, path)
                if sp:
                    if spaths is None or len(sp) < len(spaths):
                        spaths = sp
        return spaths

        # return paths


if __name__ == '__main__':
    route = [
        ('Mumbai', "Parish"),
        ("Parish", 'dubai'),
        ("Mumbai", 'dubai'),
        ("Parish", "New York"),
        ("dubai", "New York"),
        ("New York", 'Torento'),
        ('dubai', 'Kim'),
        ('Kim', 'New York')
    ]
    # Graph(route)
    g = Graph(route)
    print(g.AllPath("Mumbai", "Torento"))
