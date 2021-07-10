import sys
nums = [10, 3, 5, 6, 20]
length = len(nums)


def sol(arr, n):
    if n < 3:
        return -1
    leftmin = [-1 for i in range(n)]

    leftmax = [-1 for i in range(n)]

    rightmax = [-1 for i in range(n)]

    rightmin = [-1 for i in range(n)]

    res = -sys.maxsize
    maxsum = arr[0]
    minsum = arr[0]

    for i in range(1, n):
        leftmin[i] = minsum
        if arr[i] < minsum:
            minsum = arr[i]
        leftmax[i] = maxsum
        if arr[i] > maxsum:
            maxsum = arr[i]

    maxsum = arr[n-1]
    minsum = arr[n-1]

    for i in range(n-2, -1,-1):
        rightmax[i] = maxsum
        if arr[i] > maxsum:
            maxsum = arr[i]
        rightmin[i] = minsum
        if arr[i] < minsum:
            minsum = arr[i]
    for i in range(1, n-1):
        max1 = max(arr[i] * leftmax[i] * rightmax[i],
                   arr[i] * leftmin[i] * rightmin[i])
        max2 = max(arr[i]*leftmax[i]*rightmin[i],
                   arr[i]*leftmin[i]*rightmax[i])
        res = max(res, max(max1, max2))
    return res
print(sol(nums, length))
