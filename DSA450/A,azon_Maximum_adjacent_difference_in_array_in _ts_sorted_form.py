arr = [1, 10, 5]
length = len(arr)


def pinghole_sort(a):
    mymin = min(a)
    mymax = max(a)
    size = mymax - mymin + 1
    hole = [0] * size
    for x in a:
        hole[x - mymin] += 1
    j = 0
    for i in range(size):
        while hole[i] > 0:
            hole[i] -= 1
            arr[j] = i + mymin
            j += 1


def sol(a, n):
    pinghole_sort(a)
    res = -1e9
    for i in range(1, n):
        diff = a[i] - a[i - 1]
        res = max(res, diff)
    return res


print(sol(arr, length))
