n = 5
x = 3
y = 3
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]
dp = [[-1 for i in range(y + 1)] for j in range(x + 1)]


def dfs(arr1, arr2, tw, t1, t2):
    if tw == 0:
        return 0
    if dp[t1][t2] != -1:

        return dp[t1][t2]
    if t1 != 0 and t2 != 0:

        dp[t1][t2] = max(
            arr1[tw - 1] + dfs(arr1, arr2, tw - 1, t1 - 1, t2),
            arr2[tw - 1] + dfs(arr1, arr2, tw - 1, t1, t2 - 1)
        )
        return dp[t1][t2]

    if t2 == 0:
        dp[t1][t2] = arr1[tw - 1] + dfs(arr1, arr2, tw - 1, t1 - 1, t2)
        return dp[t1][t2]
    else:
        dp[t1][t2] = arr2[tw - 1] + dfs(arr1, arr2, tw - 1, t1, t2 - 1)
        return dp[t1][t2]


print(dfs(a, b, n, x, y))
