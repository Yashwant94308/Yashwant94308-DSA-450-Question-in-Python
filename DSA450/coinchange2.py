n = 4
m = 3
S = [1, 2, 3]
# dp = [[-1 for i in range(n + 1)] for j in range(m)]

dp = [[-1 for _ in range(n + 1)] for _ in range(m)]


def c(S, m, n):
    if m == -1 and n > 0:
        return 0
    if n == 0:
        return 1
    if n < 0:
        return 0
    if dp[m][n] != -1:
        return dp[m][n]
    else:
        dp[m][n] = c(S, m, n - S[m]) + c(S, m - 1, n)
        return dp[m][n]


print(c(S, m - 1, n))
