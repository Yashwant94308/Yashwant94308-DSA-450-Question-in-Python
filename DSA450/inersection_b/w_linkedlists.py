def findIntersection(head1,head2):
    #return head
    cur = None
    res = None
    while head1 != None and head2 != None:
        if head1.data < head2.data:
            head1 = head1.next
        elif head1.data > head2.data:
            head2 = head2.next
        else:
            temp = Node(head1.data)
            if res == None:
                res = temp
                cur = res
            else:
                cur.next = temp
                cur = temp
            head1 = head1.next
            head2 = head2.next
    return res