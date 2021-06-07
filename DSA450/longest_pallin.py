S = "cabffffdbac"


def longestPalins():
    ml = 1
    start = 0
    l = len(S)

    low = 0
    hi = 0

    for i in range(1, l):

        # even
        low = i - 1
        hi = i
        while low >= 0 and hi < l and S[low] == S[hi]:
            if hi - low + 1 > ml:
                start = low
                ml = hi - low + 1
            low -= 1
            hi += 1

        # odd
        low = i - 1
        hi = i + 1
        while low >= 0 and hi < l and S[low] == S[hi]:
            if hi - low + 1 > ml:
                start = low
                ml = hi - low + 1
            low -= 1
            hi += 1
    return S[start:start + ml]


print(longestPalins())
