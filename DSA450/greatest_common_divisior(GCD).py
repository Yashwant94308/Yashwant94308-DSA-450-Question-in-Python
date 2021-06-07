def GCD(a, b):
    if a == b or a % b == 0:
        return b
    elif b % a == 0:
        return a
    if a > b:
        return GCD(a % b, b)
    else:
        return GCD(a, b % a)


if __name__ == '__main__':
    print("GCD is", GCD(22, 99))
