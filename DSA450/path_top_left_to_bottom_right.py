m = 19
n = 71

dp = [[-1 for i in range(n + 1)] for j in range(m + 1)]


def dps(m, n):
    if m == 1 and n == 1:
        dp[m][n] = 1
        return dp[m][n]
    if m < 0 or n < 0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    dp[m][n] = dps(m - 1, n) + dps(m, n - 1)
    return dp[m][n]


print(dps(m, n)%(10**9+7))