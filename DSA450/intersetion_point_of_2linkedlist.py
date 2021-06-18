# Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1, head2):
    # code here
    f = 0
    s = 0
    ptr1 = head1
    ptr2 = head2
    while ptr1 != None:
        f += 1
        ptr1 = ptr1.next
    while ptr2 != None:
        s += 1
        ptr2 = ptr2.next
    diff = abs(f - s)
    ptr1 = head1
    ptr2 = head2
    if f > s:
        for i in range(diff):
            ptr1 = ptr1.next
    elif f < s:
        for i in range(diff):
            ptr2 = ptr2.next
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    if ptr1 != None:
        return ptr1.data
    return -1