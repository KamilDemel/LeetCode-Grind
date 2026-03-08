class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
def remove_max(head):
    if not head:
        return None
    dummy = Node(0)
    dummy.next = head
    curr = head
    max_k = curr.val
    curr = curr.next
    while curr:
        if curr.val > max_k:
            max_k = curr.val
        curr = curr.next
    curr2 = dummy
    while curr2.next:
        if curr2.next.val == max_k:
            curr2.next = curr2.next.next
            break
        curr2 = curr2.next
    return dummy.next

