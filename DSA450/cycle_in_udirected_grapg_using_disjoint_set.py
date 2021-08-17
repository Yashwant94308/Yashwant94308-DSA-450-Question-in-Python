graph = [[0, 1],
         [0, 3],
         [2, 3],
         [1, 2]
         ]
v = 4
parents = [-1] * v


def find(ver):
    if parents[ver] == -1:
        return ver
    return find(parents[ver])


def union(f, s):
    f1 = find(f)
    f2 = find(s)
    parents[f1] = f2


def is_cyclic(edges):
    for g in edges:
        f = find(g[0])
        s = find(g[1])
        if f == s:
            return True
        union(f, s)
    return False


print(is_cyclic(graph))
