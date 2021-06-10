str1 = "LSDBOFDMXJJYYFKROILT"
str2 = "UIEVCFFIGZRTRVUHCAUCL"


def slo():
    x = 20
    y = 21
    dp = [[-1 for i in range(y + 1)] for i in range(x + 1)]

    for i in range(x + 1):
        for j in range(y + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif str1[i - 1] == str2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
    return dp[x][y]


print(slo())
