class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
def solution(head1,head2):
    dummy = Node(None)
    tail = dummy
    while head1 and head2:
        if head1.val <= head2.val:
            tail.next = head1
            tail = tail.next
            head1 = head1.next
        else:
            tail.next = head2
            tail = tail.next
            head2 = head2.next
    while head1:
        tail.next = head1
        tail = tail.next
        head1 = head1.next
    while head2:
        tail.next = head2
        tail = tail.next
        head2 = head2.next
    tail.next = None
    return dummy.next
