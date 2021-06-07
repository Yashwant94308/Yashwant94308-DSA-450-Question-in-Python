def minimum_pluses(x, y):
    ans = 0
    for m in range(-1, len(x)):
        if m == -1:
            temp3 = 0
        else:
            temp3 = int(x[:m + 1])
        for i in range(m + 1, len(x)):
            temp = temp3
            temp += int(x[m + 1:i + 1])
            print('tempi', temp)
            for j in range(i + 1, len(x)):
                temp2 = temp
                temp2 += int(x[j:])
                for k in range(i + 1, j):
                    temp2 += int(x[k])
                print('temp2', temp2)
                if temp2 == int(y):
                    print('temp2', temp2)
                    ans += j
                    return ans


def main():
    A = input()
    i = 0
    while A[i] != '=':
        i += 1
    x = A[0:i]
    y = A[i + 1:]

    result = minimum_pluses(x, y)
    print(result)


if __name__ == "__main__":
    main()
