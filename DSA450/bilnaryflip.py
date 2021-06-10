s = "100"


def sol():
    def fl(e):
        return '1' if (e == '0') else '0'

    def flip(strs, exp):
        cnt = 0
        for i in strs:
            if i != exp:
                cnt += 1
            exp = fl(exp)
        return cnt

    return min(flip(s, '0'),
               flip(s, '1'))




print(sol())
