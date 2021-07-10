num2 = '4416'
num1 = '-333'


def solve(num1, num2):
    if (num1[0] == '-' or num2[0] == '-') and (num1[0] != '-' or num2[0] != '-'):
        print('-', end='')
    if num1[0] == '-' and num2[0] != '-':
        num1 = num1[1:]
    elif num1[0] != '-' and num2[0] == '-':
        num2 = num2[1:]
    elif num1[0] == '-' and num2[0] == '-':
        num1 = num1[1:]
        num2 = num2[1:]


    len1 = len(num1)
    len2 = len(num2)
    res = [0] * (len1 + len2)
    i_n1 = 0
    i_n2 = 0
    for i in range(len1 - 1, -1, -1):
        carry = 0
        n1 = ord(num1[i]) - 48
        i_n2 = 0

        for j in range(len2 - 1, -1, -1):
            n2 = ord(num2[j]) - 48
            sums = n1 * n2 + res[i_n1 + i_n2] + carry
            carry = sums // 10
            res[i_n1 + i_n2] = sums % 10
            i_n2 += 1
        if carry > 0:
            res[i_n1 + i_n2] += carry
        i_n1 += 1
    # print(res)
    i = len(res) - 1
    while i >= 0 and res[i] == 0:
        i -= 1
    if i == -1:
        return '0'
    s = ''
    while i >= 0:
        s += chr(res[i] + 48)
        i -= 1
    print(s)


solve(num1, num2)
