st = "11106"


def sol(s):
    if len(s) == 0 or s[0] == '0': return 0
    if len(s) == 1: return 1
    prev = 1
    cur = 1
    for i in range(1, len(s)):
        d = int(s[i])
        dd = int(s[i - 1:i + 1])
        cnt = 0
        if d > 0:
            cnt += cur
        if 10 <= dd <= 26:
            cnt += prev
        prev = cur
        cur = cnt
    return cur


print(sol(st))
