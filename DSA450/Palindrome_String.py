S = "abba"


def isPlaindrome():
    li = [i for i in S]
    temp = li.copy()
    li.reverse()
    if temp == li:
        return 1
    else:
        return 0


print(isPlaindrome())
