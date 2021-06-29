# Total Number of shelf
n_shelf = int(input())
# total number of query
n_q = int(input())
shelf = [[] for i in range(n_shelf)]

# queries

for i in range(n_q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        y = query[2]
        shelf[x].append(y)
    elif query[0] == 2:
        x = query[1]
        y = query[2]
        print(shelf[x][y])
    else:
        x = query[1]
        print(len(shelf[x]))


