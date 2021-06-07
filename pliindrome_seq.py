str = "abcb"
dp = [[-1 for x in range(1000)]
      for y in range(1000)]


def sol(i, j):
    # if i > j:
    #     return 0
    # # if dp[i][j] == -1:
    # #     return dp[i][j]
    # if i == j:
    #     dp[i][j] = 1
    #     return dp[i][j]
    # elif str[i] == str[j]:
    #     dp[i][j] = (sol(i + 1, j) +
    #                 sol(i, j - 1) + 1)
    #     return dp[i][j]
    # else:
    #     dp[i][j] = (sol(i + 1, j) +
    #                 sol(i, j - 1) -
    #                 sol(i + 1, j - 1))
    #     return dp[i][j]

    N = len(str)

    cps = [[0 for i in range(N + 2)] for j in range(N + 2)]

    for i in range(N):
        cps[i][i] = 1

    for L in range(2, N + 1):

        for i in range(N):
            k = L + i - 1
            if k < N:
                if str[i] == str[k]:
                    cps[i][k] = (cps[i][k - 1] +
                                 cps[i + 1][k] + 1)
                else:
                    cps[i][k] = (cps[i][k - 1] +
                                 cps[i + 1][k] -
                                 cps[i + 1][k - 1])

    return cps[0][N - 1]


n = len(str)
print(sol(0, n - 1))
