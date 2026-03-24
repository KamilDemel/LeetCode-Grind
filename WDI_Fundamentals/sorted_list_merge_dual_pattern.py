class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node


def merge_iterative(head1, head2):
    dummy = Node(-1)
    tail = dummy

    while head1 is not None and head2 is not None:
        if head1.val > head2.val:
            tail.next = head2
            head2 = head2.next
        else:
            tail.next = head1
            head1 = head1.next
        tail = tail.next
    if head1 is not None:
        tail.next = head1
    else:
        tail.next = head2

    return dummy.next


def merge_recursive(head1, head2):
    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.val < head2.val:
        head1.next = merge_recursive(head1.next, head2)
        return head1
    else:
        head2.next = merge_recursive(head1, head2.next)
        return head2