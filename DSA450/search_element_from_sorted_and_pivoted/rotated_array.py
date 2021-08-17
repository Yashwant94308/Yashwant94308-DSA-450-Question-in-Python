array = [4, 5, 6, 7, 8, 9, 1, 2, 3]
key = 7


def binary_search(arr, keys):
    lo = 0
    hi = len(arr)
    while lo <= hi:
        mid = (lo + hi) // 2
        # print(mid)
        if arr[mid] == key:
            return mid
        if arr[mid] >= arr[lo]:
            if arr[lo] <= keys <= arr[mid]:
                hi = mid - 1
            else:
                lo = mid + 1
        elif arr[mid] <= keys <= arr[hi]:
            hi = mid + 1
        else:
            lo = mid - 1

    return -1


if binary_search(array, key) == -1:
    print('Not Found')
else:
    print('found')
