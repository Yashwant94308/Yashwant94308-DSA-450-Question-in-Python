nums = [2, 7, 9, 3, 1]
n = len(nums)


def dfs(i, v):
    if i == n:
        return v
    if i > n:
        return v
    mf = dfs(i + 2, v + nums[i])

    ms = dfs(i + 1, v)

    return max(mf, ms)


print(dfs(0, 0))
