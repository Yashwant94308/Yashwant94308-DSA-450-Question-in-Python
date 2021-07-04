arr1 = [8, 15, 3, 7]
n = len(arr1)
dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]


def osg(arr, i, j):
    if i == j:
        dp[i][j] = arr[i]
        return dp[i][j]
    if i + 1 == j:
        dp[i][j] = max(arr[i], arr[j])
        return dp[i][j]
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = max(arr[i] + min(osg(arr, i + 2, j), osg(arr, i + 1, j - 1)),
                   arr[j] + min(osg(arr, i + 1, j - 1), osg(arr, i, j - 2)))
    return dp[i][j]


print(osg(arr1, 0, n - 1))
