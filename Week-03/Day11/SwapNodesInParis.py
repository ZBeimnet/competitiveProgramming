# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def swap_nodes_in_paris(head):
    start = head.next

    prev = head.next
    curr = prev.next
    nxt = curr.next
    while curr.next is not None:
        prev.next = nxt
        curr.next = nxt.next
        nxt.next = curr

        prev = nxt
        curr = prev.next
        nxt = curr.next



    while head is not None:
        print(head.val, end=" -> ")


    # return start


h = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)

h.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

swap_nodes_in_paris(h)
