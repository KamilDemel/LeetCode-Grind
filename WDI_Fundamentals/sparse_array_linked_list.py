class Node:
    def __init__(self, value, index, next_node=None):
        self.value = value
        self.index = index
        self.next = next_node


def get_val(head, index):
    curr = head
    while curr:
        if curr.index == index:
            return curr.value
        curr = curr.next
    return 0


def set_val(head, index, value):
    curr = head
    while curr:
        if curr.index == index:
            curr.value = value
            return head
        curr = curr.next
    new_node = Node(value, index)
    new_node.next = head
    return new_node