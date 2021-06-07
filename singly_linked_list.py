class Node:
    def __init__(self, data=None, nex=None):
        self.next = nex
        self.data = data


class Linked_list:
    def __init__(self):
        self.head = None

    def length_of_linked_list(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at_starting(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data)

    def insert_at_middle(self, data, loc_value):

        if self.head is None:
            print("Location Not Found and Inserted as First Element")
            node = Node(data)
            self.head = node
            return
        flag = True
        itr = self.head
        while itr:
            if itr.data == loc_value:
                flag = False
                break
            itr = itr.next
        if flag:
            print("Location  not found, not inserted a middle")
            return
        else:
            node = Node(data, itr.next)
            itr.next = node

    def insert_through_index(self, data, ind):
        index = ind - 1
        if index < 0 or index > self.length_of_linked_list():
            print("index out of range :", index)
            return
        if index == 0:
            node = Node(data, self.head)
            self.head = node
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def remove_through_index(self, ind):

        index = ind - 1
        if index < 0 or index > self.length_of_linked_list():
            print("index out of range :", index)
            return
        if index == 0:
            self.head = self.head.next
            return
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

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
    l_list.insert_at_end(100)
    l_list.insert_at_end(102)
    l_list.insert_at_starting(103)
    l_list.insert_at_middle(105, 103)
    l_list.insert_at_middle(106, 103)
    l_list.insert_at_middle(102, 102)
    l_list.insert_through_index(111, 6)
    l_list.remove_through_index(3)
    l_list.insert_at_starting(19)

    l_list.print_data()
