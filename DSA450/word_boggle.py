n = 4
dic = ['GEEKS', 'FOR', 'QUIZ', 'GO']
board = [['G', 'I', 'Z'],
         ['U', 'E', 'K'],
         ['Q', 'S', 'E']]

R = len(board)
C = len(board[0])


def dfs(word, wi, r, c, vis):
    # print(vis)
    if R <= r or r < 0 or C <= c or c < 0 or vis[r][c] != -1:
        return False
    # print(wi)
    if wi >= len(word) :
        return False
    # print(board[r][c], r, c)
    if word[wi] != board[r][c]:
        return False
    if wi == len(word) - 1:
        return True
    vis[r][c] = 1
    one = dfs(word, wi + 1, r + 1, c, vis)
    two = dfs(word, wi + 1, r, c + 1, vis)
    three = dfs(word, wi + 1, r - 1, c, vis)
    four = dfs(word, wi + 1, r, c - 1, vis)
    five = dfs(word, wi + 1, r + 1, c + 1, vis)
    six = dfs(word, wi + 1, r - 1, c - 1, vis)
    seven = dfs(word, wi + 1, r + 1, c - 1, vis)
    eight = dfs(word, wi + 1, r - 1, c + 1, vis)
    vis[r][c] = -1
    if one == True or two == True or three or four or five or six or seven or eight:
        return True
    return False


ans = []
for word in dic:
    vis = [[-1 for i in range(C + 1)] for j in range(R + 1)]
    for r in range(R):
        for c in range(C):
            if board[r][c] == word[0]:

                if dfs(word, 0, r, c, vis):
                    ans.append(word)
print(ans)
