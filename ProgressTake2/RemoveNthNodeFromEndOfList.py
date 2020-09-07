# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        current = head
        count = 0

        # counting the nodes
        while current:
            count += 1
            current = current.next

        # checking if we're removing the first node
        if count == n:
            return head.next

        # removing the node
        current = head
        pos = count - n - 1
        start = 0
        while current:
            if start == pos:
                current.next = current.next.next
                return head
            start += 1
            current = current.next
