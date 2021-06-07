import sys
sys.setrecursionlimit(10000)
def Game(player, start, end, song):

    if len(player) == 1:
        print(player[0])

    elif song[start] == 'x':
        temp = player.pop(0)
        player.append(temp)
        if start == end:
            Game(players, 0, len(S) - 1, S)
        else:

            Game(players, start + 1, len(S) - 1, S)
    else:
        player.pop(0)

        if start == end:
            Game(players, 0, len(S) - 1, S)
        else:

            Game(players, start + 1, len(S) - 1, S)


if __name__ == '__main__':
    N = int(input())
    S = input()
    players = list(i for i in range(1, N+1))

    Game(players, 0, len(S) - 1, S)
