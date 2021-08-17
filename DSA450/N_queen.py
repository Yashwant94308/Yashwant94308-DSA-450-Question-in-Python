n = 4
board = [['.'] * n for i in range(n)]

rows = set()
positive_diagonal = set()
negative_diagonal = set()
res = []


def recur(c):
    if c == n:
        cop = ["".join(roww) for roww in board]
        res.append(cop)
        return
    for r in range(n):
        if r in rows or (r + c) in positive_diagonal or (r - c) in negative_diagonal:
            continue
        rows.add(r)
        positive_diagonal.add(r + c)
        negative_diagonal.add(r - c)
        board[r][c] = 'Q'
        recur(c + 1)
        rows.remove(r)
        positive_diagonal.remove(r + c)
        negative_diagonal.remove(r - c)
        board[r][c] = "."


recur(0)
# print(res)
ans = []
for result in res:
    temp = []
    for elem in result:
        for i in range(len(elem)):
            if elem[i] == 'Q':
                temp.append(i+1)

    ans.append(temp)
ans.sort()
print(ans)
