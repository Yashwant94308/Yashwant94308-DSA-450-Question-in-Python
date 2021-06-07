class Car:
    def __init__(self, s, u):
        self.s = s
        self.u = u

    def __repr__(self):
        m = 'Car with the maximum speed of ' + str(self.s) + " " + str(self.u)
        return repr(m)


class Boat:
    def __init__(self, s, ):
        self.s = s

    def __repr__(self):
        m = 'Boat with the maximum speed of ' + str(self.s)
        return repr(m)


v = Boat(222)
print(v)