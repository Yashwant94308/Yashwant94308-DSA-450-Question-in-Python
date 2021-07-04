n = 500


# using recursion
# formula c0 = 1, res += c[i]*c[n-i-1]
# time complex o(2**n)

# def catalan(n):
#     if n <= 1:
#         return 1
#     res = 0
#     for i in range(n):
#         res += catalan(i) * catalan(n - 1 - i)
#     return res
#
#
# for i in range(n + 1):
#     print(catalan(i))


# using DP
# tim complex o(n**2)

# def catalan(n):
#     if n <= 1:
#         return 1
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     dp[1] = 1
#
#     for i in range(2, n+1):
#         for j in range(i):
#             dp[i] += dp[j] * dp[i - 1 - j]
#     return dp[n]
#
#
# for j in range(n + 1):
#     print(catalan(j), end=' ')


# binomial coffie
# time complex o(n)

def bc(n, k):
    if k > n - k:
        k = n - k
    res = 1
    for i in range(k):
        res = res * (n - i)
        res = res // (i + 1)
    return res


def ct(n):
    c = bc(2 * n, n)
    return c // (n + 1)


for i in range(n + 1):
    print(ct(i))
