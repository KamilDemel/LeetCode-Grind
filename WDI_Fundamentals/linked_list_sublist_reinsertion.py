class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def fix_unsorted_sublist(head):
    """
    Finds a point where the list stops being sorted, extracts a sublist
    starting from that point, and reinserts it in the correct position.
    """
    if not head or not head.next:
        return head

    dummy = Node(None, head)
    curr = head

    while curr and curr.next:
        if curr.next.val <= curr.val:
            sublist_start = curr.next
            sublist_end = sublist_start

            for _ in range(5):
                if sublist_end.next:
                    sublist_end = sublist_end.next

            curr.next = sublist_end.next

            search_ptr = dummy
            while search_ptr.next:
                if search_ptr.next.val > sublist_start.val:
                    sublist_end.next = search_ptr.next
                    search_ptr.next = sublist_start
                    return dummy.next
                search_ptr = search_ptr.next

        curr = curr.next

    return dummy.next