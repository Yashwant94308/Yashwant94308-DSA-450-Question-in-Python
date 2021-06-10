strr = 'AABBBCBB'
stt = set(strr)

## recursion

# def check(s, st):
#     li = []
#     if len(s) == 0:
#         return False
#     if len(st) == 0:
#         return False
#     for i in s:
#         if i not in st:
#             return False
#         else:
#             li.append(i)
#     if len(set(li)) == len(st):
#         return True
#     else:
#         return False
#
#
# def recur(s, st):
#     dp = [[1e9 for i in range(len(s))] for i in range(len(s))]
#     ans = 1e9
#     for i in range(len(s)):
#         for j in range(len(s)):
#
#             if j == 0 and i == 0:
#                 dp[i][j] = 109
#
#             elif check(s[i:j], st) and len(s[i:j]) >= len(st):
#                 ans = len(s[i:j])
#
#                 return min(ans, dp[i])
#             else:
#                 return ans
#
#
# print(recur(strr, stt))


# window sliding
from collections import defaultdict


def ws(s, st):
    n = len(s)
    disc = len(st)
    curr_cnt = defaultdict(lambda: 0)
    cnt = 0
    start = 0
    min_len = n
    for i in range(n):
        curr_cnt[s[i]] += 1
        if curr_cnt[s[i]] == 1:
            cnt += 1
        if cnt == disc:
            while curr_cnt[s[start]] > 1:
                if curr_cnt[s[start]] > 1:
                    curr_cnt[s[start]] -= 1
                start += 1
            len_w = i - start + 1
            if len_w < min_len:
                min_len = len_w
                start_index = start
    return min_len
print(ws(strr, stt))