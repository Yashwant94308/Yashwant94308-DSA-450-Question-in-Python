a = [7, 10, 4, 20, 15]
k = 4
length = len(a)


def heap(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    if left < len(arr) and arr[left] > arr[largest]:
        largest = left
    if right < len(arr) and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        t = arr[largest]
        arr[largest] = arr[i]
        arr[i] = t
        heap(arr, largest)


def heap_insert(arr, elem):
    arr.insert(0, elem)
    heap(arr, 0)


def pop_heap(tree):
    elm = tree[0]
    last = tree.pop(-1)
    if len(tree) > 0:
        tree[0] = last
        heap(tree, 0)
    return elm


def sol(arr, n, x):
    heap_li = []
    for i in range(n):
        if len(heap_li) == 0:
            heap_li.append(arr[i])
        elif len(heap_li) < x:
            heap_insert(heap_li, arr[i])

        elif len(heap_li) >= x:

            if heap_li[0] > arr[i]:
                temp = pop_heap(heap_li)
                heap_insert(heap_li, arr[i])
    return heap_li[0]


print(sol(a, length, k))
