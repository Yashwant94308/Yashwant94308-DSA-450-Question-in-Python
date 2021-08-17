a = [4, 5, 7, 8, 0, 1, 2]
target = 2


def solve(arr, n, x):
    lo = 0
    hi = n - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] >= arr[lo]:
            if arr[mid] >= x >= arr[lo]:
                hi = mid - 1
            else:
                lo = mid + 1
        else:
            if arr[mid] <= x <= arr[hi]:
                lo = mid + 1
            else:
                hi = mid - 1
    return 'Not Found'


print(solve(a, len(a), target))
