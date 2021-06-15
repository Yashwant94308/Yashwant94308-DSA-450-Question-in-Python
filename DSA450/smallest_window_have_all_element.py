S = "geeksforgeeks"
P = "ork"


def check(strr, ppp):
    if len(strr) == 0 or len(ppp) == 0 or len(ppp) > len(strr):
        return False
    strd = list(strr)
    for i in ppp:
        if i not in strd:
            return False
        strd.remove(i)

    return True


li = []


def sol(st, pat, start, end):
    if check(st, pat):
        ans = len(st)
        li.append([ans, start, end])
        return min(ans, sol(st[1:], pat, start + 1, end), sol(st[:-1], pat, start, end - 1))

    else:
        return 1e9


a = (sol(S, P, 0, len(S)))
li.sort()
if len(li) > 0:
    strt = li[0][1]
    end = li[0][2]
    print(S[strt: end])
else:
    print(-1)
