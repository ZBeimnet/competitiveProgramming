import heapq
from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = [(-nums[i], i) for i in range(k - 1)]
        heapq.heapify(max_heap)
        result = []
        
        for i in range(k - 1, len(nums)):
            heapq.heappush(max_heap, (-nums[i], i))
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            result.append(-max_heap[0][0])
        
        return result