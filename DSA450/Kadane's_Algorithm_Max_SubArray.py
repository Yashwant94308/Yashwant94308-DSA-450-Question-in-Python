N = 14
arr = [74, -72, 94, -53, -59, -3, -66, 36, -13, 22, 73, 15, -52, 75]


def maxSubarraySum():
    end = updated = 0

    for i in range(0, N):
        end += arr[i]
        if updated < end:
            updated = end
        if end < 0:
            end = 0

    return updated


print(maxSubarraySum())
