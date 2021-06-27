coins = [2,3,4,5]

amount = 130050
dp = [1e9] * (amount + 1)
dp[0] = 0

# dp
def dpD():
    for i in range(amount + 1):
        for c in coins:
            if i-c >= 0:
                dp[i] = min(dp[i], 1+dp[i-c])


dpD()
# print(dp)
if dp[amount] == 1e9 or dp[amount] == 1e9 - 1:
    print(-1)
else:
    print(dp[amount])

# recursive
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
