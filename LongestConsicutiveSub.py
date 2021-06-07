arr = [8, 9, 1, 2, 3, 1]


def long():
    s = set(arr)
    b = list(s)
    cnt = 1
    ans = 0
    for i in range(len(b) - 1):
        if b[i] + 1 == b[i + 1]:
            cnt += 1
            ans = max(ans, cnt)

        else:
            ans = max(ans, cnt)
            cnt = 1

    return ans


print(long())
