a = [8, 3, 2, 7, 4, 6, 8]


def pingHole(arr):
    mymax = max(arr)
    mymin = min(arr)
    size = mymax - mymin + 1

    hole = [0] * size
    for i in arr:
        hole[i - mymin] += 1
    j = 0
    for i in range(size):
        while hole[i] > 0:
            hole[i] -= 1
            arr[j] = i + mymin
            j += 1


pingHole(a)
print(a)
