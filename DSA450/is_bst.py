# Python program to check if a binary tree is bst or not

INT_MAX = 4294967296
INT_MIN = -4294967296


class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBST(node):
    return isBSTUtil(node, INT_MIN, INT_MAX)


def isBSTUtil(node, mini, maxi):
    # An empty tree is BST

    if node is None:
        return True

    print(node.data, mini, maxi)

    # False if this node violates min/max constraint
    if node.data < mini or node.data > maxi:
        return False

    # Otherwise check the subtrees recursively
    # tightening the min or max constraint
    return (isBSTUtil(node.left, mini, node.data - 1) and
            isBSTUtil(node.right, node.data + 1, maxi))


root = Node(100)
root.left = Node(50)
root.right = Node(200)
root.left.left = Node(25)
root.left.right = Node(75)
root.right.left = Node(125)
root.right.right = Node(350)

if isBST(root):
    print("Is BST")
else:
    print("Not a BST")
