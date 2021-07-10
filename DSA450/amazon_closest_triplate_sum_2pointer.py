nums = [-1, 2, 1, -4]
target = 1


def solve(arr, n, x):
    res = 1e9
    arr.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if abs(x - s) < abs(x - res):
                res = s
            if s > x:
                right -= 1
            else:
                left += 1
    return res


print(solve(nums, len(nums), target))
