import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.min_heap = nums[:self.k]
        heapq.heapify(self.min_heap)

        for i in range(self.k, len(nums)):
            if self.min_heap[0] < nums[i]:
                heapq.heapreplace(self.min_heap, nums[i])

    def add(self, val: int) -> int:
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        elif self.min_heap[0] < val:
            heapq.heapreplace(self.min_heap, val)

        return self.min_heap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)