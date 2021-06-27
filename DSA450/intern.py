# import sys
# 
# sys.setrecursionlimit(100000)
# li = ['1', '2', '3', '4']
# 
# n = len(li)
# 
# cnt = [0]
# 
# 
# def permu(arr, l, r, ):
#     if l == r:
#         print(arr, end=" ")
#         # cnt[0] += 1
#         # print(cnt)
# 
#     else:
#         for i in range(l, r):
#             arr[l], arr[i] = arr[i], arr[l]
#             permu(arr, l + 1, r)
#             arr[i], arr[l] = arr[l], arr[i]
# 
# 
# permu(li, 0, n)
N = 3
w = 4
dp = [[0 for i in range(w + 1)] for j in range(N + 1)]


def sol(W, wt, val, n):
    if n == 0 or W == 0:
        return 0
    if dp[n][W] != 0:
        return dp[n][W]
    if wt[n - 1] > W:
        dp[n][W] = sol(W, wt, val, n - 1)
        return dp[n][W]

    else:
        dp[n][W] = max(val[n - 1] + sol(W - wt[n - 1], wt, val, n - 1), sol(W, wt, val, n - 1))
        return dp[n][W]


if __name__ == '__main__':

    values = [1, 2, 3]
    weight = [4, 5, 1]
    print(sol(w, weight, values, N))
