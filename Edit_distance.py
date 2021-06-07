t = "sunday"
s = "saturday"


# def ed_rec(str1, str2, m, n):
#     if n == 0:
#         return m
#     if m == 0:
#         return n
#     if str1[m - 1] == str2[n - 1]:
#         return ed_rec(str1, str2, m - 1, n - 1)
#
#     return 1 + min(ed_rec(str1, str2, m, n - 1),
#                    ed_rec(str1, str2, m - 1, n),
#                    ed_rec(str1, str2, m - 1, n - 1))
#
#
# print(ed_rec(s, t, len(s), len(t)))


# def ed_dp(str1, str2, m, n):
#     dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
#
#     for i in range(m + 1):
#         for j in range(n + 1):
#             if i == 0:
#                 dp[i][j] = j
#             elif j == 0:
#                 dp[i][j] = i
#             elif str1[i - 1] == str2[j - 1]:
#                 dp[i][j] = dp[i - 1][j - 1]
#             else:
#                 dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])
#     return dp[m][n]
#
#
# print(ed_dp(s, t, len(s), len(t)))


def ed_dp_less_space(str1, str2):
    len1 = len(str1)
    len2 = len(str2)

    # Create a DP array to memoize result
    # of previous computations
    DP = [[0 for i in range(len1 + 1)]
          for j in range(2)]

    # Base condition when second String
    # is empty then we remove all characters
    for i in range(0, len1 + 1):
        DP[0][i] = i

    # Start filling the DP
    # This loop run for every
    # character in second String
    for i in range(1, len2 + 1):

        # This loop compares the char from
        # second String with first String
        # characters
        for j in range(0, len1 + 1):

            # If first String is empty then
            # we have to perform add character
            # operation to get second String
            if j == 0:
                DP[i % 2][j] = i

            # If character from both String
            # is same then we do not perform any
            # operation . here i % 2 is for bound
            # the row number.
            elif str1[j - 1] == str2[i - 1]:
                DP[i % 2][j] = DP[(i - 1) % 2][j - 1]

            # If character from both String is
            # not same then we take the minimum
            # from three specified operation
            else:
                DP[i % 2][j] = (1 + min(DP[(i - 1) % 2][j],
                                        min(DP[i % 2][j - 1],
                                            DP[(i - 1) % 2][j - 1])))

    # After complete fill the DP array
    # if the len2 is even then we end
    # up in the 0th row else we end up
    # in the 1th row so we take len2 % 2
    # to get row
    print(DP[len2 % 2][len1], "")


ed_dp_less_space(s, t)
