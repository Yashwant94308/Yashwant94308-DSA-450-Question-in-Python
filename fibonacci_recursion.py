def fib(n):

    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':

    for i in range(int(input())):
        print(fib(i+1), end=" ")
