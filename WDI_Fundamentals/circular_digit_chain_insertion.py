class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def get_first_digit(n):
    temp = abs(n)
    while temp >= 10:
        temp //= 10
    return temp


def get_last_digit(n):
    return abs(n) % 10


def insert_into_chain(head, element):
    if not head:
        return 0

    start_node = head
    is_first_lap = True
    new_val_first = get_first_digit(element)
    new_val_last = get_last_digit(element)

    curr_start = head
    while curr_start != start_node or is_first_lap:
        is_first_lap = False

        if get_last_digit(curr_start.val) == new_val_first:
            scan_node = curr_start
            is_scan_lap = True
            distance = 0

            while scan_node != curr_start or is_scan_lap:
                is_scan_lap = False

                if new_val_last == get_first_digit(scan_node.next.val):
                    if distance >= 2:
                        new_node = Node(element)
                        new_node.next = scan_node.next
                        curr_start.next = new_node
                        return distance

                distance += 1
                scan_node = scan_node.next

        curr_start = curr_start.next
    return 0