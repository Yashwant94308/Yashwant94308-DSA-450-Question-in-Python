str = 'ix'


def r_to_n(s):
    dic = {"I": 1,
           "V": 5,
           'X': 10,
           'L': 50,
           'C': 100,
           'D': 500,
           'M': 1000}
    n = len(s)
    s = s.upper()
    i = 1
    ans = dic[s[0]]
    while i < n:
        if dic[s[i - 1]] < dic[s[i]]:
            if i == 1:
                ans = dic[s[i]] - ans
            else:
                ans -= dic[s[i - 1]]
                ans += (dic[s[i]] - dic[s[i - 1]])

            i += 1
        else:
            ans += dic[s[i]]
            i += 1

    print(ans)


r_to_n(str)
