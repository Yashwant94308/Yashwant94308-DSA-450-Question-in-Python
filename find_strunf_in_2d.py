class GFG:

    def __init__(self):
        self.R = None
        self.C = None
        self.dir = [[-1, 0], [1, 0], [1, 1],
                    [1, -1], [-1, -1], [-1, 1],
                    [0, 1], [0, -1]]

    def search2D(self, grid, row, col, word):

        if grid[row][col] != word[0]:
            return False

        for x, y in self.dir:

            rd, cd = row + x, col + y
            flag = True

            for k in range(1, len(word)):

                if (0 <= rd < self.R and
                        0 <= cd < self.C and
                        word[k] == grid[rd][cd]):

                    rd += x
                    cd += y
                else:
                    flag = False
                    break

            if flag:
                return True
        return False

    def patternSearch(self, grid, word):

        # Rows and columns in given grid
        self.R = len(grid)
        self.C = len(grid[0])

        # Consider every point as starting point
        # and search given word
        fnd = []
        for row in range(self.R):
            for col in range(self.C):
                if self.search2D(grid, row, col, word):
                    fnd.append([row, col])
        return fnd


# Driver Code
if __name__ == '__main__':
    grid = ["GEEKSFORGEEKS",
            "GEEKSQUIZGEEK",
            "IDEQAPRACTICE"]
    gfg = GFG()
    print(gfg.patternSearch(grid, 'GEEKS'))
    print('')
    print(gfg.patternSearch(grid, 'EEE'))

# This code is contributed by Yezheng Li
