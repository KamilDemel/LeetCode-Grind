class ListNode:
    def __init__(self, val, next=None):
         self.val = val
         self.next = next
def copy_list(head):
    dummy = ListNode(None)
    tail = dummy
    curr = head
    while curr:
        nowy_wezel = ListNode(curr.val)
        tail.next = nowy_wezel
        tail = tail.next
        curr = curr.next
    return dummy.next
def solution(head):
    kopia_heada = copy_list(head)
    dummy = ListNode(None)
    tail = dummy
    curr = head
    prev = None
    head_ctr = head
    ctr = 0
    while head_ctr:
        ctr += 1
        head_ctr = head_ctr.next
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head_reversed = prev
    head_normal = kopia_heada
    ctr_new = 0
    while head_normal and head_reversed and ctr_new < ctr:
        tail.next = head_normal
        tail = tail.next
        tail.next = head_reversed
        tail = tail.next
        head_normal = head_normal.next
        head_reversed = head_reversed.next
        ctr_new += 2
    tail.next = None
    kopia_heada = dummy.next
    return kopia_heada
def solution_v2(head):
    if not head:
        return
    fast = head
    slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    druga_polowa = slow.next
    slow.next = None
    prev = None
    while druga_polowa:
        nxt = druga_polowa.next
        druga_polowa.next = prev
        prev = druga_polowa
        druga_polowa = nxt
    start_1_half = head
    start_2_half = prev
    while start_2_half:
        nxt1 = start_1_half.next
        nxt2 = start_2_half.next
        start_1_half.next = start_2_half
        start_1_half = nxt1
        start_2_half.next =  start_1_half
        start_2_half = nxt2






