import sys

arr = [1,3,1,5,8,1]
n = len(arr)

# using DP
dp = [[-1 for i in range(n + 1)] for j in range(n + 1)]


def dfs(arr, i, j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    # dp[i][j] = sys.maxsize
    for k in range(i, j):
        dp[i][j] = max(dp[i][j], dfs(arr, i, k) + dfs(arr, k + 1, j) + (arr[i - 1] * arr[k] * arr[j]))
    return dp[i][j]


print(dfs(arr, 1, n - 1))

# using Recursion
# def dfs(arr, i, j):
#     if i == j:
#         return 0
#     _min = sys.maxsize
#     for k in range(i, j):
#         cnt = dfs(arr, i, k) + dfs(arr, k+1, j) + (arr[i-1]*arr[k]*arr[j])
#         if cnt < _min:
#             _min = cnt
#     return _min
#
# print(dfs(arr, 1, n-1))
