class Node:
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


def vertical_traverse(root):
    if root is None:
        return
    q = [root]
    qhd = {}
    qhd[root] = 0
    m = {}
    m[0] = [root.data]
    while len(q) > 0:
        node = q.pop(0)
        if node.left:
            q.append(node.left)
            qhd[node.left] = qhd[node] - 1
            hd = qhd[node.left]
            if m.get(hd) is None:
                m[hd] = []
            m[hd].append(node.left.data)
        if node.right:
            q.append(node.right)
            qhd[node.right] = qhd[node] + 1
            hd = qhd[node.right]
            if m.get(hd) is None:
                m[hd] = []
            m[hd].append(node.right.data)
    sot = sorted(m.items())

    for _, li in sot:
        for i in li:
            print(i, " ", end='')
        print()


# def ino(roo):
#     if roo:
#         print(roo.data)
#         ino(roo.left)
#
#         ino(roo.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.left.right = Node(8)
root.right.right.left = Node(10)
root.right.right.right = Node(9)
root.right.right.left.right = Node(11)
root.right.right.left.right.right = Node(12)
print("Vertical order traversal is ")
# ino(root)
vertical_traverse(root)
