string = "ofrsgkeeeekgs"
lene = len(string)


def encode(s, n):
    if n == 1:
        return s
    if n == 2:
        ans = ''
        for i in range(n - 1, -1, -1):
            ans += s[i]
        return ans
    ans = s[0]
    for i in range(1, n):
        if i % 2 == 0:
            ans = ans + s[i]
        else:
            ans = s[i] + ans

    return ans


print(encode(string, lene))
