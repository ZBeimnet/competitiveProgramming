# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # finding the middle node
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reversing the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt

        # checking if they are palindrome (here, node is always the smaller one)
        while node:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
