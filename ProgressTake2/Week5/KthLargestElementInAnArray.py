"""
* keep a heap with length k
* add number if greater than top of k
* finally the kth largest would be at the top of k
"""
import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for num in nums:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif min_heap[0] <= num:
                heapq.heapreplace(min_heap, num)

        return heapq.heappop(min_heap)