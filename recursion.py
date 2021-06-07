def sum_of_ten_numbers(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n + sum_of_ten_numbers(n - 1)


if __name__ == '__main__':
    print(sum_of_ten_numbers(998))
