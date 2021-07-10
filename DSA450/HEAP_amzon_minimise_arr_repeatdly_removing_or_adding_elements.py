arr = [1, 3, 7, 5, 6]
n = len(arr)


def heapify(tree, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(tree) and tree[left] < tree[largest]:
        largest = left
    if right < len(tree) and tree[right] < tree[largest]:
        largest = right
    if largest != i:
        t = tree[largest]
        tree[largest] = tree[i]
        tree[i] = t
        heapify(tree, largest)


def heap_insert(tree, elm):
    tree.insert(0, elm)
    heapify(tree, 0)


def heap_pop(tree):
    elm = tree[0]
    last = tree.pop(-1)
    if len(tree) > 0:
        tree[0] = last
        heapify(tree, 0)
    return elm


def solve(tree):
    if len(tree) < 1:
        return tree[:]
    max_cnt = 0
    while len(tree) > 1:
        a = heap_pop(tree)
        b = heap_pop(tree)
        temp = a + b
        max_cnt += temp
        heap_insert(tree, temp)
    return max_cnt
print(solve(arr))


