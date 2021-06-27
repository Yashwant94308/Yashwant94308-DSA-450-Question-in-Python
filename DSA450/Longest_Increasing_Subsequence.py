nums = [1, 3, 7]
n = len(nums)

# N2 time complexity
# dp = [1] * n
#
# for i in range(n-1, -1, -1):
#     for j in range(i+1, n):
#         if nums[i] < nums[j]:
#             dp[i] = max(dp[i], 1+dp[j])
# print(max(dp))

# NlogN time complexity
import bisect

dp = [1e9] * (n + 1)
dp[0] = -1e9
for i in range(n):
    idx = bisect.bisect_right(dp, nums[i])
    # print(idx)
    if dp[idx - 1] < nums[i] < dp[idx]:
        dp[idx] = nums[i]
ma = 0
print(dp)
for i in range(n, -1, -1):
    if dp[i] != 1e9:
        ma = i
        break

print(ma)
