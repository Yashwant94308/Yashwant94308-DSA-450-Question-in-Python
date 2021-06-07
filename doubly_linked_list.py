class Node:
    def __init__(self, data=None, nex=None, prev=None):
        self.next = nex
        self.prev = prev
        self.data = data


class Linked_list:
    def __init__(self):
        self.head = None

    def insert_at_starting(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data, self.head)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, nex=None, prev=itr)

    def remove_at_beg(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next
        self.head.prev = None

    def print_data(self):
        if self.head is None:
            print("list is empty.")
            return
        itr = self.head
        li = ""
        while itr:
            li += str(itr.data) + " --> "
            itr = itr.next
        print(li)


if __name__ == '__main__':
    l_list = Linked_list()

    l_list.insert_at_starting(89)
    l_list.insert_at_starting(9)
    l_list.insert_at_starting(99)
    l_list.insert_at_end(101)
    l_list.insert_at_end(1)
    l_list.insert_at_end(111)
    l_list.insert_at_starting(919)
    l_list.remove_at_beg()
    l_list.insert_at_starting(22)
    l_list.insert_at_starting(23)
    l_list.remove_at_beg()
    l_list.insert_at_starting(91)
    l_list.print_data()
