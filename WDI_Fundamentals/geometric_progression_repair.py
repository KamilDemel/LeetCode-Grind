class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def geometric_gcd(a, b):
    while abs(a - b) > 0.0000001:
        if abs(a) > abs(b):
            a = a / b
        else:
            b = b / a
    return a


def repair_geometric_list(head):
    if not head or not head.next:
        return 0

    curr = head
    common_ratio = curr.next.val / curr.val
    curr = curr.next
    inserted_count = 0

    temp = head
    while temp.next:
        current_ratio = temp.next.val / temp.val
        common_ratio = geometric_gcd(common_ratio, current_ratio)
        temp = temp.next

    curr = head
    while curr.next:
        if abs((curr.next.val / curr.val) - common_ratio) < 0.00000001:
            curr = curr.next
        else:
            missing_val = curr.val * common_ratio
            new_node = Node(missing_val)
            inserted_count += 1
            new_node.next = curr.next
            curr.next = new_node
            curr = curr.next

    return inserted_count