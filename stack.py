from collections import deque


class Stack:
    def __init__(self):
        self.stk = deque()

    def push(self, data):
        self.stk.append(data)

    def pop(self):
        if self.is_empty():
            return "UNDER FLOW"
        else:
            return self.stk.pop()

    def peak(self):
        if self.is_empty():
            return "UNDER FLOW"
        else:
            return self.stk[-1]

    def is_empty(self):
        return len(self.stk) == 0

    def stack_length(self):
        return len(self.stk)

    def print_stack(self):
        fs = self.stk.copy()
        fs.reverse()
        for i in fs:
            print(i, end=" ")
        print()


if __name__ == '__main__':
    s = Stack()
    s.push(56)
    s.push(6)
    s.push(5)
    s.push(8)
    s.print_stack()
    s.push(78)
    s.print_stack()
    s.push(61)
    s.push(57)
    s.push(89)
    s.print_stack()
