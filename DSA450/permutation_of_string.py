from collections import Counter

__count = 0


def swap(s, i, j):
    s[i], s[j] = s[j], s[i]

    return s


def total_permutation_without_rep(s):
    n = total_permutation(len(s))
    temp = 1
    dic = Counter(s)
    for k, v in dic.items():
        temp *= total_permutation(v)

    return "{:.2f}".format(n / temp)


def total_permutation(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * total_permutation(n - 1)


def permutation_string_using_rec(s, i, n):
    global __count
    if i == n:
        __count += 1
        print(s, __count)
    else:
        for j in range(i, n):
            s = swap(s, i, j)
            permutation_string_using_rec(s, i + 1, n)
            s = swap(s, i, j)


if __name__ == '__main__':
    h = input()

    f = list(h[:])
    # permutation_string_using_rec(f, 0, len(f))
    # print(__count)
    __count = total_permutation(len(f))
    print("with repeat", __count)
    __count = total_permutation_without_rep(f)

    print("with out repeat:", __count)
