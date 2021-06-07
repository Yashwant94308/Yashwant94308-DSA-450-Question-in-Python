f = [3, 5, 4, 3]


def frw():
    cnt = 0
    n = len(f)
    for i in range(n):
        cnt += (f[i] // 2)
        f[i] = f[i] % 2
    i = 0
    j = 1
    while i < n and j < n:
        if f[i] + f[i+1] == 2:
            cnt += 1
            i += 2
            j += 2
        else:
            i += 1
            j += 1
    return cnt

print(frw())
