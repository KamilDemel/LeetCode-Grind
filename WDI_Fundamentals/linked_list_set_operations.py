class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def add_to_set(head, val):
    curr = head
    while curr:
        if curr.val == val:
            return head
        curr = curr.next
    new_node = Node(val)
    new_node.next = head
    return new_node


def remove_from_set(head, val):
    if head is None:
        return None
    if head.val == val:
        return head.next
    prev = head
    curr = head.next
    while curr:
        if curr.val == val:
            prev.next = curr.next
            return head
        prev = curr
        curr = curr.next
    return head