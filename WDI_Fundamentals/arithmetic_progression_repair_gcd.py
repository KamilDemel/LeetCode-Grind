class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def repair_arithmetic_list(head):
    if not head or not head.next:
        return 0

    curr = head
    diff = abs(curr.next.val - curr.val)
    temp = head.next
    while temp.next:
        current_gap = abs(temp.next.val - temp.val)
        diff = gcd(diff, current_gap)
        temp = temp.next

    inserted_count = 0
    temp = head
    while temp.next:
        if temp.next.val - temp.val == diff:
            temp = temp.next
        else:
            new_val = temp.val + diff
            new_node = Node(new_val)
            inserted_count += 1
            new_node.next = temp.next
            temp.next = new_node
            temp = temp.next

    return inserted_count