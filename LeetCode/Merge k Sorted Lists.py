import heapq
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
def mergeKLists(lists):
    pq = []
    dummy = ListNode(-1)
    tail = dummy
    licznik = 0
    for heads in lists:
        if heads:
            heapq.heappush(pq,(heads.val,licznik+1,heads))
            licznik += 1
    while pq:
        curr_val, licznik,curr_node = heapq.heappop(pq)
        tail.next = curr_node
        tail = tail.next
        curr_node = curr_node.next
        if curr_node:
            heapq.heappush(pq,(curr_node.val,licznik+1,curr_node))
            licznik += 1
    return dummy.next

