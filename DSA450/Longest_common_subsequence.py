# @ LCS
text1 = "aeiaaioaaaaeiiiiouuuooaauuaeiu"
text2 = 'aeiou'
dp = [[0 for j in range(len(text2)+1)] for i in range(len(text1)+1)]
for i in range(len(text1)+1):
    for j in range(len(text2) + 1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif text1[i-1] == text2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[len(text1)][len(text2)])
# dp = [['' for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
# for i in range(len(text1) + 1):
#     for j in range(len(text2) + 1):
#         if i == 0 or j == 0:
#             dp[i][j] = ''
#         elif text1[i - 1] == text2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + text1[i - 1]
#         else:
#             dp[i][j] = dp[i][j-1] if len(dp[i][j-1]) > len(dp[i-1][j]) else dp[i-1][j]
# print(dp[len(text1)][len(text2)])
