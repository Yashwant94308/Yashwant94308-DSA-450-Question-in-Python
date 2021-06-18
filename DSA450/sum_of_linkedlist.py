class Solution:
    def addOne(self, head):
        # Returns new head of linked List.

        def rev(head):
            nex = None
            prev = None
            cur = head
            while cur != None:
                nex = cur.next
                cur.next = prev
                prev = cur
                cur = nex
            return prev

        def one(head):
            # ll = LinkedList()
            head = rev(head)
            cur = head
            while cur != None:
                if cur.next == None and cur.data == 9:
                    cur.data = 1
                    temp = Node(0)
                    temp.next = head
                    head = temp
                    cur = cur.next
                elif cur.data == 9:
                    cur.data = 0
                    cur = cur.next
                else:
                    cur.data = cur.data + 1
                    cur = cur.next
                    break
            head = rev(head)
            return head

        return (one(head))