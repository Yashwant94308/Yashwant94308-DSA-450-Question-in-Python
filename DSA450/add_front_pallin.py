strings = 'ABC'


def sol(string):
    m = len(string)
    lbs = [-1] * m
    length = 0
    lbs[0] = 0
    i = 1
    while i < m:
        if string[i] == string[length]:
            length += 1
            lbs[i] = length
            i += 1
        else:
            if length != 0:
                length = lbs[length - 1]
            else:
                lbs[i] = 0
                i += 1
    return lbs


def main():
    revStr = strings[::-1]
    concat = strings + "$" + revStr
    lps = sol(concat)
    return len(strings) - lps[-1]


print(main())
