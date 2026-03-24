import math


class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


def get_prime_squares(limit):
    T = [True] * (limit + 1)
    T[0] = False
    T[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if T[i]:
            for j in range(i * i, limit + 1, i):
                T[j] = False

    result = []
    for i in range(len(T)):
        if T[i]:
            square = i * i
            result.append(square)
    return result


prime_squares_list = get_prime_squares(100)


def divide_list(head):
    dummy1 = Node(-3)
    dummy2 = Node(-8)
    tail1 = dummy1
    tail2 = dummy2
    curr = head

    while curr:
        is_divisible_by_square = False
        for i in range(len(prime_squares_list)):
            if curr.val % prime_squares_list[i] == 0 and curr.val > prime_squares_list[i]:
                is_divisible_by_square = True
                tail1.next = curr
                tail1 = tail1.next
                break

        if not is_divisible_by_square:
            tail2.next = curr
            tail2 = tail2.next

        curr = curr.next

    tail1.next = None
    tail2.next = None
    return dummy1.next, dummy2.next


def convert_to_linked_list(py_list):
    dummy = Node(-3)
    tail = dummy
    for i in range(len(py_list)):
        element = Node(py_list[i])
        tail.next = element
        tail = tail.next
    return dummy.next


def print_list(head):
    while head:
        print(head.val)
        head = head.next