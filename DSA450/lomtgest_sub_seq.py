def lss(a, b):

    m = [[0]*(len(b)+1) for _ in range(len(a)+1)]
    
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if i == 0 or j == 0:
                m[i][j] = 0
            elif a[i-1] == b[j-1]:
                m[i][j] = 1 + m[i - 1][j - 1]
            else:
                m[i][j] = max(m[i - 1][j], m[i][j - 1])
    
    print(m[-1][-1])


if __name__ == '__main__':
    lss('ABCDGH', 'AEDFHR')
    lss('AGGTAB', 'GXTXAYB')
