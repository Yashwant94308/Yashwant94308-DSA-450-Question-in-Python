class Node:
    def __init__(self, data, next=None):
        self.next = next
        self.data = data


class ll:
    def __init__(self):
        self.head = None

    def insert(self, data):
        a = Node(data)
        a.next = self.head
        self.head = a

    def insert_between(self, data):
        cur = self.head
        cnt = 1
        a = Node(data)
        while cur is not None:
            if cnt == 3:
                a.next = cur
                cur = a
                break
            cnt += 1
            cur = cur.next

    def prints(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next


root = ll()
root.insert(1)
root.insert(2)
root.insert(3)
root.insert(6)
root.insert(5)
root.insert(4)
root.insert_between(6)
root.prints()
