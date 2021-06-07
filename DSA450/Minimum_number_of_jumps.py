n = int(input('n: '))
arr = []


def minJumps():
    if n <= 1:
        return 0
    if arr[0] == 0:
        return -1
    maxr = arr[0]
    stp = arr[0]
    j = 1
    for i in range(1, n):
        if i == n - 1:
            return j
        maxr = max(maxr, i + arr[i])
        stp -= 1
        if stp == 0:
            j += 1
            if i >= maxr:
                return -1
            stp = maxr - i
    return -1


for _ in range(n):
    arr.append(int(input()))
result = minJumps()
print(result)
