# S = 'bcdebeae'
S = 'aabb'


def sol(s, i, st, n):
    a = ''
    if st > n:
        return a
    if s[st] == i:
        a += i 


print(sol(S, S[0], 1, len(S)-1))
