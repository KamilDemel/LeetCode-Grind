class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def solution(head,k):
    dummy = ListNode(-1)
    tail = dummy
    def reverse_list(start):
        prev = None
        curr = start
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev
    curr = head
    while curr:
        kth = curr
        for _ in range(k-1):
            if kth:
                kth = kth.next
        if not kth:
            tail.next = curr
            break
        next_chunk = kth.next
        kth.next = None
        new_head = reverse_list(curr)
        tail.next = new_head
        tail = curr
        curr = next_chunk
    return dummy.next