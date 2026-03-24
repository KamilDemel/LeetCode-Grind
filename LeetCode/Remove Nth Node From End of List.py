class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
def remove(head, n):
    dummy = Node(0)
    dummy.next = head
    curr = head
    ctr = 0
    while curr:
        ctr+=1
        curr = curr.next
    ctr2 = 0
    curr2 = dummy
    while curr2.next:
        if ctr - n == ctr2:
            curr2.next = curr2.next.next
            break
        curr2 = curr2.next
        ctr2+=1
    return dummy.next