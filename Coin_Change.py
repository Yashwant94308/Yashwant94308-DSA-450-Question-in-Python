coins = [1, 3, 4, 5]
amount = 7
res = [1e9]


def dfs(arr, n, t, cnt):
    if t == 0:
        res[0] = min(res[0], cnt)
        return
    if t < 0 or n < 0:
        return
    cnt += 1
    # print(cnt)
    dfs(arr, n, t - arr[n], cnt)
    cnt -= 1
    # print(cnt)
    dfs(arr, n - 1, t, cnt)


dfs(coins, len(coins) - 1, amount, 0)
print(res[0])
