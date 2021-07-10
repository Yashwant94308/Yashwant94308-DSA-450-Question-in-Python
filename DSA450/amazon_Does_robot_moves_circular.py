path = "GRGRGRG"


def isCircular(path):
    # code here
    N = 0
    E = 1
    S = 2
    W = 3
    x = 0
    y = 0
    dir = N
    for i in path:
        move = i
        if move == 'R':
            dir = (dir + 1) % 4
        elif move == 'L':
            dir = (4 + dir - 1) % 4
        else:
            if dir == N:
                y += 1
            elif dir == E:
                x += 1
            elif dir == S:
                y -= 1
            else:
                x -= 1
    if x == 0 and y == 0:
        return 'Circular'
    else:
        return "Not Circular"


print(isCircular(path))
