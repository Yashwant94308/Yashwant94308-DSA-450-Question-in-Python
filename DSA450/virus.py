def test(v, bl):
    if len(bl) > len(v):
        return "NEGATIVE"
    i = 0
    j = 0
    while i < len(bl) and j < len(v):

        if bl[i] == v[j]:
            i += 1
            j += 1
        else:
            j += 1
    if i >= len(bl):

        return "POSITIVE"
    else:

        return "NEGATIVE"


def main():
    v = input()
    n = int(input())

    for _ in range(n):
        bl = input()
        print(test(v, bl))


main()
