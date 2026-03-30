class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
def sol(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev
def sol_reku(head):
    if not head or not head.next:
        return head
    new_head = sol_reku(head.next)
    head.next.next = head
    head.next = None
    return new_head