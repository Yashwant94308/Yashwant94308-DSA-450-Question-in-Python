total_char = 256


def bd_hurestic(pat, m):
    bc = [-1] * total_char
    for i in range(m):
        bc[ord(pat[i])] = i
    return bc


def search(txt, pat):
    m = len(pat)
    n = len(txt)

    badchar = bd_hurestic(pat, m)

    s = 0
    while s <= n - m:
        j = m - 1
        while j >= 0 and pat[j] == txt[j + s]:
            j -= 1
        if j < 0:
            print('patter occur at', s)

            s += (m - badchar[ord(txt[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - badchar[ord(txt[s + j])])


def main():
    txt = "ABAAABCDABCABCABCABC"
    pat = "ABC"
    search(txt, pat)


if __name__ == '__main__':
    main()
