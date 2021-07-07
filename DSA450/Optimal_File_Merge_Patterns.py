arr1 = [2, 3, 4, 5, 6, 7]


def ofm(arr):
    cnt = 0
    while len(arr) > 1:
        arr.sort()
        a = arr.pop(0)
        b = arr.pop(0)

        temp = a + b
        cnt += temp
        arr.insert(0, temp)
    return cnt


print(ofm(arr1))
