str1 = "abac"
str2 = "cab"

def Lcs(text1, text2):
    dp = [['' for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
    for i in range(len(text1) - 1, -1, -1):
        for j in range(len(text2) - 1, -1, -1):
            if text1[i] == text2[j]:
                dp[i][j] = text1[i] + dp[i + 1][j + 1]
            else:
                dp[i][j] = dp[i][j+1] if len(dp[i][j+1]) > len(dp[i+1][j]) else dp[i+1][j]
    return dp[0][0]


def scs(text1, text2):
    lcs = Lcs(text1, text2)
    # print(lcs)
    i = 0
    j = 0
    ans = ''
    for lc in lcs:
        while text1[i] != lc:
            ans += text1[i]
            i += 1
        while text2[j] != lc:
            ans += text2[j]
            j += 1
        ans += lc
        i += 1
        j += 1
    ans += text1[i:]
    ans += text2[j:]
    return ans


print(scs(str1, str2))
