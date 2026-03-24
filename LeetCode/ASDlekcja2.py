class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next
def add(head,p):
    if not head:
        return None
    new_val = p.val
    temp = head
    if temp.val > new_val:
        p.next = head
        return p
    while temp.next:
        if temp.next.val >= new_val:
            p.next = temp.next
            temp.next = p
            return head
        else:
            temp = temp.next
    temp.next = p
    return head
