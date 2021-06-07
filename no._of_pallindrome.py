from math import floor

arr = [121, 131, 920292029]
n = 3


def pl():
    for i in arr:
        s = str(i)
        i = 0
        j = len(s)-1
        while i < j and j > i:
            if s[i] == s[j]:
                i += 1
                j -= 1
                
            else:
                return 0
    return 1
print(pl())