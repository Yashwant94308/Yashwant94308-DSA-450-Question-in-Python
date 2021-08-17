import sys

l = 1
r = 10
tar = 2


# res = [0]
#
#
# def dfs(nums, k, cnt):
#     if nums < l or nums > r:
#         return
#     if k == 0 and cnt % 2 == 0:
#         res[0] += 1
#         return
#     if k <= 0:
#         return
#     for i in range(l, r + 1):
#         dfs(i, k - 1, cnt + i)
#
#
# dfs(l, tar, 0)
# print(res)

# efficient approach
def solve(lo, hi, k):
    evn_cnt = hi / 2 - (lo - 1) / 2
    odd_cnt = (hi + 1) / 2 - lo / 2

    evn_sm = 1
    odd_sm = 0
    for i in range(0, k):
        prev_evn = evn_sm
        prev_odd = odd_sm

        evn_sm = ((prev_evn * evn_cnt) + (prev_odd * odd_cnt))
        odd_sm = ((prev_evn * odd_cnt) + (prev_odd * evn_cnt))
    return int(evn_sm)


print(solve(l, r, tar))
