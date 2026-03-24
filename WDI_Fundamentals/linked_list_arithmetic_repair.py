class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def repair_arithmetic_sequence(head):
    """
    Finds the smallest difference between adjacent nodes and 'repairs'
    the sequence by inserting missing values to maintain that difference.
    """
    if not head or not head.next:
        return 0

    curr = head
    min_diff = float("inf")
    while curr.next:
        diff = curr.next.val - curr.val
        if diff < min_diff:
            min_diff = diff
        curr = curr.next

    curr = head
    inserted_count = 0
    while curr.next:
        if curr.next.val - curr.val > min_diff:
            new_node = Node(curr.val + min_diff)
            new_node.next = curr.next
            curr.next = new_node

            inserted_count += 1
            curr = curr.next
        else:
            curr = curr.next

    return inserted_count