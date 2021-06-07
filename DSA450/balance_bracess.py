s = "}{{}}{{{"


def sol():
    if len(s) % 2 != 0:
        return -1
    li = []
    cnt = 0
    for i in s:
        if len(li) == 0:
            li.append(i)
        elif li[-1] == "{" and i == "}":
            li.pop()
        else:
            li.append(i)
    if len(li) == 0:
        return cnt
    else:
        i = 0
        j = len(li)
        while i < j:
            a = li.pop()
            b = li.pop()
            if (a == "{" and b == "{") or (a == "}" and b == "}"):
                cnt += 1
            else:
                cnt += 2
            i += 2
    return cnt

print(sol())


