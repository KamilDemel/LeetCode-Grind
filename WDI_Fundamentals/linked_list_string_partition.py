class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def is_increasing(text):
    if not text: return True
    for i in range(len(text) - 1):
        if ord(text[i]) >= ord(text[i + 1]):
            return False
    return True


def is_decreasing(text):
    if not text: return True
    for i in range(len(text) - 1):
        if ord(text[i]) <= ord(text[i + 1]):
            return False
    return True


def partition_and_link(head):
    dummy_inc = Node(None)
    dummy_dec = Node(None)
    dummy_other = Node(None)

    tail_inc = dummy_inc
    tail_dec = dummy_dec
    tail_other = dummy_other

    current = head
    while current:
        next_node = current.next
        current.next = None

        if is_increasing(current.val):
            tail_inc.next = current
            tail_inc = tail_inc.next
        elif is_decreasing(current.val):
            tail_dec.next = current
            tail_dec = tail_dec.next
        else:
            tail_other.next = current
            tail_other = tail_other.next

        current = next_node

    sep1 = Node("")
    sep2 = Node("")

    tail_inc.next = sep1
    sep1.next = dummy_other.next
    tail_other.next = sep2
    sep2.next = dummy_dec.next

    return dummy_inc.next
