sticks = [2, 4, 3]


# result = 14

def sol():
    cost = 0
    sticks.sort()
    while len(sticks) > 1:
        a = sticks.pop(0)
        b = sticks.pop(0)
        s = a + b
        sticks.insert(0, s)
        cost += s
    return cost


print(sol())
