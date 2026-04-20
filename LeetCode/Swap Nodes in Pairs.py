class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def soluton(head):
    dummy = ListNode(-1)
    tail = dummy
    def reverse(start):
        prev = None
        curr = start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    while head and head.next:
        curr = head.next.next
        head.next.next = None
        new_head = reverse(head)
        head.next = curr
        tail.next = new_head
        tail = head
        head = curr
    return dummy.next

