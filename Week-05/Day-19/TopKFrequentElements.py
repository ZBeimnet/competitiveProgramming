import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        count = {}
        for i in range(length):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        max_heap = []
        for i in count:
            max_heap.append([count[i], i])

        heapq._heapify_max(max_heap)

        result_list = []
        for i in range(k):
            result_list.append(heapq._heappop_max(max_heap)[1])

        return result_list





