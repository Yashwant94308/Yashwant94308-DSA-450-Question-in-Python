nums = [1, 2, 3, 1]


def rob1(arr):
    # n = len(arr)
    r1, r2 = 0, 0
    for i in arr:
        t = max(i + r1, r2)
        r1 = r2
        r2 = t
    return r2


if len(nums) == 1:
    print(nums[0])
else:
    fs = rob1(nums[:-1])
    snd = rob1(nums[1:])
    print(max(fs, snd))
