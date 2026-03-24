class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def reorder_by_parity(head):
    dummy_even = Node(None)
    dummy_odd = Node(None)

    tail_even = dummy_even
    tail_odd = dummy_odd

    curr = head
    while curr:
        if curr.val % 2 == 1:
            tail_odd.next = curr
            tail_odd = tail_odd.next
        else:
            tail_even.next = curr
            tail_even = tail_even.next
        curr = curr.next

    tail_odd.next = dummy_even.next
    tail_even.next = None

    return dummy_odd.next