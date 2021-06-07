arr = [4, 11, 6, 5, 11, 20, 19, 14, 14, 2, 9, 20, 11, 11, 15, 1, 7, 12, 19, 9]
n = len(arr)
k = 14


def minSwap():
    cnt = 0
    for i in arr:
        if i <= k:
            cnt += 1
    bad = 0
    for j in range(cnt):
        if arr[j] > k:
            bad += 1
    ans = bad
    j = cnt
    for i in range(n):
        if j == n:
            break
        if arr[i] > k:
            bad -= 1
        if arr[j] > k:
            bad += 1
        ans = min(ans, bad)
        j += 1
    return ans


print(minSwap())
print(arr)
