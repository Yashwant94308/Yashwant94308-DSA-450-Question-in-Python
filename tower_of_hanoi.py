__count = 0


def t_o_h(n, beg, aux, end):
    global __count
    if n >= 1:
        t_o_h(n - 1, beg, end, aux)
        print(beg, "--->", end)
        __count += 1
        t_o_h(n - 1, aux, beg, end)


if __name__ == '__main__':
    t_o_h(3, 'a', 'b', 'c')
    print(__count)
