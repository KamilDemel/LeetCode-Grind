class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
def delete(curr):
    head = curr
    while head.next:
        if head.next.val == head.val:
            head.next = head.next.next
        else:
            head = head.next
    return curr
