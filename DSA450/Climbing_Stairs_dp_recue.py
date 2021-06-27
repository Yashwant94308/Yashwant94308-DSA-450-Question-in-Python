n = 5
dp = [-1]*(n+1)
# print(dp)
import time
st = time.time()
def dfs(s):
    one = 1
    two = 1
    for i in range(s-1):
        t = one
        one = one + two
        two = t
    return one


print(dfs(n))
end = time.time()
print("time taking by for loops to find min and max", end - st)

# # dp sol
# dp = [-1]*(n+1)
# # print(dp)
# import time
# st = time.time()
# def dfs(s):
#     if s == 0:
#         return 1
#     if s < 0:
#         return 0
#     if dp[s] != -1:
#         return dp[s]
#     dp[s] = dfs(s - 1) + dfs(s - 2)
#     # print(ans)
#     return dp[s]


# recursion
# def dfs(s):
#     if s == 0:
#         return 1
#     if s < 0:
#         return 0
#     ans = dfs(s - 1) + dfs(s - 2)
#     # print(ans)
#     return ans