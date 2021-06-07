arr = [-8, 6, -3, -10, 0, 2]


def maxProduct():
    minVal = arr[0]
    maxval = arr[0]
    ans = arr[0]
    for i in range(1, len(arr)):
        if arr[i] < 0:
            temp = minVal
            minVal = maxval
            maxval = temp
        minVal = min(arr[i], arr[i]*minVal)
        maxval = max(arr[i], arr[i]*maxval)
        ans = max(ans, maxval)
    return ans



print(maxProduct())
