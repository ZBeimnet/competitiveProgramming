# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        # checking for input
        if not head:
            return
        if k == 1:
            return head

        # counting number of nodes in the linked-list
        current_node = head
        node_count = 0
        while current_node:
            node_count += 1
            current_node = current_node.next

        last_k_group = node_count - node_count % k
        new_head = head
        start = head
        end = None
        prev = head
        curr = prev.next
        count = 2
        while count <= last_k_group:
            temp = curr.next
            if count % k == 0:
                if count == k:
                    new_head = curr
                elif end:
                    end.next = curr
                end = start
                curr.next = prev
                start.next = temp
                start = temp
                prev = temp
                if temp:
                    curr = temp.next
                count += 1
            else:
                curr.next = prev
                prev = curr
                curr = temp
            count += 1

        return new_head
