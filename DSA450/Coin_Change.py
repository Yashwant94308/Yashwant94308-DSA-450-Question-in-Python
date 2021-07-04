coins = [1, 2, 3]
m = len(coins)
n = amount = 4
dp = [1e9] * (amount + 1)
dp[0] = 0


# print(dp)
# dp
def dpD():
    for i in range(amount + 1):
        for c in coins:
            if i - c >= 0:
                dp[i] = min(dp[i], 1 + dp[i - c])


dpD()
# print(dp)
if dp[amount] == 1e9 or dp[amount] == 1e9 - 1:
    print(-1)
else:
    print(dp[amount])
# dp tabular
# dp = [[-1 for _ in range(n + 1)] for _ in range(m)]
#
#
# def c(S, m, n):
#     if m == -1 and n > 0:
#         return 0
#     if n == 0:
#         return 1
#     if n < 0:
#         return 0
#     if dp[m][n] != -1:
#         return dp[m][n]
#     else:
#         dp[m][n] = c(S, m, n - S[m]) + c(S, m - 1, n)
#         return dp[m][n]
#
#
# print(c(coins, m - 1, n))

# recursive
# res=[0]
# def dfs(arr, n, t, cnt):
#     if t == 0:
#         res[0] = min(res[0], cnt)
#         return
#     if t < 0 or n < 0:
#         return
#     cnt += 1
#     # print(cnt)
#     dfs(arr, n, t - arr[n], cnt)
#     cnt -= 1
#     # print(cnt)
#     dfs(arr, n - 1, t, cnt)
#
#
# dfs(coins, len(coins) - 1, amount, 0)
# print(res[0])
