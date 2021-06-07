s = "aaaa"


def kmp():
    n = len(s)
    lbs = [0] * n
    left = 0
    i = 1

    while i < n:
        if s[i] == s[left]:
            left += 1
            lbs[i] = left
            i += 1
        else:
            if left != 0:
                left = lbs[left - 1]
            else:
                lbs[i] = 0
                i += 1
    ans = lbs[n - 1]
    return ans


print(kmp())
