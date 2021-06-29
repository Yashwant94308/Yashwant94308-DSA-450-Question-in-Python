row = 3
col = 2
dp = [[0 for i in range(col+1)] for j in range(row+1)]
# dp approach
# dp[row-1][col-1] = 1
for i in range(row-1, -1, -1):
    for j in range(col-1, -1,-1):
        if i == row-1 and j == col-1:
            dp[i][j] = 1
            continue
        dp[i][j] = dp[i+1][j] + dp[i][j+1]
print(dp[0][0])




# li = [0]

# recursion backtracking

# def sol(r, c):
#     if r == row-1 and c == col-1:
#         li[0] += 1
#         return 1
#     if r > row-1 or c > col-1:
#         return 0
#     dp[r][c] = sol(r + 1, c)
#     dp[r][c] = sol(r, c + 1)
#
#
# sol(0, 0)
# print(li)
# print("dp\n", dp)
