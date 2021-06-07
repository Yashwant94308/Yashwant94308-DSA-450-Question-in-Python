arr = [3, 6, 6, 9, 12, 12, 14, 14, 15, 16, 16, 20, 22, 22, 23, 24, 25, 25, 26, 27, 27, 27, 28, 28, 30, 30, 30, 30, 31,
       35, 36, 36, 37, 37, 38, 41, 43, 44, 46, 47, 50, 51, 57, 57, 58, 59, 60, 63, 63, 63, 64, 65, 68, 68, 68, 68,
       69, 70, 71, 71, 73, 74, 74, 77, 78, 79, 81, 82, 83, 83, 85, 85, 87, 87, 88, 89, 91, 92, 93, 94, 94, 96, 97, 99]
# arr = [1, 3, 4, 7, 9, 9, 12, 56]
n = len(arr)
m = 61


def findMinDiff():
    if m == 0:
        return 0
    arr.sort()

    if m == 1:
        return arr[0]
    print(arr)
    maxi = 0
    mini = 0
    ans = 1e9
    i = m
    j = 0
    while i < n:
        mini = arr[j]
        maxi = arr[i - 1]
        ans = min(ans, (maxi - mini))
        if maxi - mini >= arr[i] - arr[j + 1]:
            i += 1
            j += 1
        else:
            i += 1
            j += 1
    return ans


print(findMinDiff())
