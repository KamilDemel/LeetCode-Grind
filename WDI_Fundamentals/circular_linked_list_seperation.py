class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def separate_circular_list(head):
    if not head:
        return None, None, 0

    curr = head
    dummy_positive_even = Node(None)
    dummy_negative_odd = Node(None)

    tail1 = dummy_positive_even
    tail2 = dummy_negative_odd
    ignored_count = 0
    start = True

    while curr != head or start:
        start = False

        if curr.val > 0 and curr.val % 2 == 0:
            tail1.next = curr
            tail1 = tail1.next
        elif curr.val < 0 and curr.val % 2 == 1:
            tail2.next = curr
            tail2 = tail2.next
        else:
            ignored_count += 1

        curr = curr.next

    tail1.next = dummy_positive_even.next
    tail2.next = dummy_negative_odd.next

    return dummy_positive_even.next, dummy_negative_odd.next, ignored_count