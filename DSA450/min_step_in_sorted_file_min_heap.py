n = 6
size = [2, 3, 4, 5, 6, 7]


def min_heap(arr, i):
    left = 2 * i + 1
    right = 2 * i + 2
    if left < len(arr) and arr[left] < arr[i]:
        s = left
    else:
        s = i
    if right < len(arr) and arr[right] < arr[s]:
        s = right
    if s != i:
        arr[i], arr[s] = arr[s], arr[i]
        min_heap(arr, s)


def heap_pop(arr):
    if len(arr) == 0:
        return -1e9
    mi = arr[0]
    last = arr.pop(-1)
    arr[0] = last
    min_heap(arr, 0)
    return mi


def heap_insert(arr, elem):
    arr.insert(0, elem)
    min_heap(arr, 0)


def sol(arr):
    merged = 0
    while len(arr) > 1:
        if len(arr) <= 2:
            a = arr.pop(0)
            b = arr.pop(0)
        else:
            a = heap_pop(arr)
            b = heap_pop(arr)
        merged += (a + b)
        heap_insert(arr, (a + b))
    return merged

print(sol(size))
