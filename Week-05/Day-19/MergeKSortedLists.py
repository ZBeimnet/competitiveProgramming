import heapq
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return

        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, [lists[i].val, i])

        if len(min_heap) == 0: return

        head_val = heapq.heappop(min_heap)
        head_node = current_node = ListNode(head_val[0])
        lists[head_val[1]] = lists[head_val[1]].next

        if lists[head_val[1]]:
            heapq.heappush(min_heap, [lists[head_val[1]].val, head_val[1]])

        while len(min_heap) > 0:
            current_val = heapq.heappop(min_heap)
            current_node.next = ListNode(current_val[0])
            lists[current_val[1]] = lists[current_val[1]].next

            if lists[current_val[1]]:
                heapq.heappush(min_heap, [lists[current_val[1]].val, current_val[1]])

            current_node = current_node.next

        return head_node


