def l_c_s(a, b, m, n):
    if m == 0 or n == 0:
        return 0
    elif a[m - 1] == b[n - 1]:
        return 1 + l_c_s(a, b, m - 1, n - 1)
    else:
        return max(l_c_s(a, b, m - 1, n), l_c_s(a, b, m, n - 1))


if __name__ == '__main__':
    i, j = ('AGGTAB', 'GXTXAYB')

    print(l_c_s(i, j, len(i), len(j)))
