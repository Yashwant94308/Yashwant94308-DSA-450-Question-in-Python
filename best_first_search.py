succList = {'A': [['B', 32], ['C', 23], ['D', 35]],
            'B': [['A', 40], ['E', 19]],
            'C': [['A', 40], ['E', 19], ['F', 17], ['D', 35]],
            'D': [['A', 40], ['C', 25], ["F", 17]],
            'F': [['C', 25], ['D', 35], ['G', 0]],
            'G': [['F', 17], ['H', 10]],
            'E': [['C', 25], ['B', 32], ['H', 10]],
            'H': [['G', 0], ['E', 19]]}

Start = 'A'
Goal = 'G'
closed_list = ['A']
open_list = succList['A']


def GoalState(n):
    if n == Goal:
        return True
    else:
        return False


def B_F_S():
    for i in range(len(succList)):
        if len(open_list) == 0:
            print('not reachable')
            break
        # print(open_list)
        open_list.sort(key=lambda x: x[1])

        if GoalState(open_list[0][0]):
            closed_list.append(open_list[0][0])
            for m in range (len(closed_list)):
                if m == len(closed_list)-1:
                    print(closed_list[m])
                    break
                else:
                    print(closed_list[m], end='-->')
            break
        else:
            temp = open_list[0][0]
            closed_list.append(open_list[0][0])
            open_list.remove(open_list[0])
            for j in succList[temp]:
                open_list.append(j)


B_F_S()