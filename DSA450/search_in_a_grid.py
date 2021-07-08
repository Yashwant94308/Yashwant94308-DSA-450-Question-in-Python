grid = ["GEEKSFORGEEKS",
        "GEEKSQUIZGEEK",
        "IDEQAPRACTICE"]
word = "EEE"

direction = [[-1, 0], [1, 0], [0, 1], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
R = len(grid)
C = len(grid[0])


def search(grid, row, col, word):
    if grid[row][col] != word[0]:
        return False
    for x, y in direction:
        rd = row + x
        cd = col + y
        flag = True
        for i in range(1, len(word)):
            if 0 <= rd < R and 0 <= cd < C and word[i] == grid[rd][cd]:
                rd += x
                cd += y
            else:
                flag = False
                break
        if flag:
            return True
    return False


def sol():
    fnd = []
    for i in range(R):
        for j in range(C):
            if search(grid, i, j, word):
                fnd.append([i, j])
    return fnd


print(sol())
