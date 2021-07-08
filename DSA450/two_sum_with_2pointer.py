arr = [48, 24, 99, 51, 33, 39, 29, 83, 74, 72, 22, 46, 40, 51, 67, 37, 78, 76, 26, 28, 76, 25, 10, 65, 64, 47, 34, 88, 26, 49, 86, 73, 73, 36, 75, 5, 26, 4, 39, 99, 27, 12, 97, 67, 63, 15, 3, 92, 90]

arr.sort()


def pairedElements(arr, tar):
    lo = 0
    hi = len(arr) - 1
    res = []
    while lo < hi:
        if arr[lo] + arr[hi] == tar:
            res.append([arr[lo], arr[hi]])
        if arr[lo] + arr[hi] > tar:
            hi -= 1
        else:
            lo += 1
    return res


print(pairedElements(arr, 50))
