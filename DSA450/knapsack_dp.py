val = [60, 100, 120]
wt = [10, 20, 30]
W = 50


def knapsack():
    n = len(val)
    dp = [[0 for i in range(W+1)] for j in range(n+1)]
    # print(dp)
    for i in range(n+1):
        for w in range(W+1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif wt[i-1] > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
    print(dp[n][W])

knapsack()