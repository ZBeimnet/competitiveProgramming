# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        num1 = l1
        num2 = l2
        new_head = current = ListNode((num1.val + num2.val) % 10)
        rem = (num1.val + num2.val) // 10
        num1 = num1.next
        num2 = num2.next

        while num1 or num2:
            value1 = num1.val if num1 else 0
            value2 = num2.val if num2 else 0
            new_node = ListNode((value1 + value2 + rem) % 10)
            rem = (value1 + value2 + rem) // 10

            current.next = new_node
            current = current.next
            num1 = num1.next if num1 else None
            num2 = num2.next if num2 else None

        if rem != 0:
            current.next = ListNode(rem)

        return new_head
