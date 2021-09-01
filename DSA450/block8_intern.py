class q:
    def __init__(self):
        self.q1 = []
        self.q2 = []

    def en(self, val):

        while len(self.q1) != 0:
            self.q2.append(self.q1[0])
            self.q1.pop(0)
        self.q1.append(val)

        while len(self.q2) != 0:
            self.q1.append(self.q2[0])
            self.q2.pop(0)

    def dq(self):
        if len(self.q1) == 0:
            print('empty')
        return self.q1.pop(0)


qq = q()
qq.en(1)
qq.en(2)
print(qq.dq())
