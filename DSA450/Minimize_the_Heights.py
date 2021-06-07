k = int(input('k: '))
n = int(input('n: '))
arr = []


def getMinDiff():
    arr.sort()
    mxs = []
    mns = []
    for i in arr:
        mxs.append(i + k)
        mns.append(i - k)
    ans = arr[-1] - arr[0]

    for i in range(1, n):
        if mns[i] >= 0:
            ans = min(ans, max(mns[n - 1], mxs[i - 1]) - min(mns[i], mxs[0]))

    return ans


for _ in range(n):
    temp = int(input())
    arr.append(temp)
result = getMinDiff()
print(result)
