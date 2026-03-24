class ListNode:
    def __init__(self,val,next = None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, head1, head2):
        dummy = ListNode(-1)
        tail = dummy
        carry = 0
        while head1 or head2 or carry == 1:
            if head1:
                val1 = head1.val
            else:
                val1 = 0
            if head2:
                val2 = head2.val
            else:
                val2 = 0
            val1 = val1 + carry
            suma = (val1 + val2) % 10
            if val1 + val2 > 9:
                carry = 1
            else:
                carry = 0
            tail.next = ListNode(suma)
            tail = tail.next
            if head1:
                head1 = head1.next
            if head2:
                head2 = head2.next
        return dummy.next

