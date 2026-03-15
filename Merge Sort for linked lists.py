class Node:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
def merge(head1,head2):
    dummy = Node(0)
    curr = dummy
    while head1 and head2:
        if head1.val > head2.val:
            curr.next = head2
            head2 = head2.next
        else:
            curr.next = head1
            head1 = head1.next
        curr = curr.next
    if head1:
        curr.next = head1
    if head2:
        curr.next = head2
    return dummy.next
def cut(head):
    curr = head
    while curr.next and curr.next.val >= curr.val:
        curr = curr.next
    reszta = curr.next
    curr.next = None
    return reszta
def merge_Sort(head):
    kolejka = []
    while head:
        curr = cut(head)
        kolejka.append(head)
        head = curr
    while len(kolejka) > 1:
        lista1 = kolejka.pop(0)
        lista2 = kolejka.pop(0)
        res = merge(lista1,lista2)
        kolejka.append(res)
    return kolejka[0]
