def binary(n, l):
    if n < 1:
        print(l)
    else:
        l[n - 1] = '0'
        binary(n - 1, l)
        l[n - 1] = '1'
        binary(n - 1, l)


if __name__ == '__main__':
    m = []
    binary(10, m)
