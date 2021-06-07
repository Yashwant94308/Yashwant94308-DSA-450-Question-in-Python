''' Read input from STDIN. Print your output to STDOUT '''


# Use input() to read input from STDIN and use print to write your output to STDOUT
def prime(o):
    if o == 0:
        return False
    if o == 1:
        return False
    if o == 2:
        return True
    for i in range(2, o):
        if o % i == 0:
            return False
    return True


def is_prime(l, r):
    low = 0
    high = 0
    l_flag = True
    r_flag = True
    if l == r:
        return 0


    while l < r and r > l:

        if prime(l) and l_flag:
            low = l
            l_flag = False
        if prime(r) and r_flag:
            high = r
            r_flag = False
        l += 1
        r -= 1

    if low == 0 and high == 0:
        return -1
    else:
        return high - low


def main():
    # Write code here
    n = int(input())
    for _ in range(n):
        l, r = [int(x) for x in input().split()]

        print(is_prime(l, r))


main()
