"""
[2,7,4,1,8,1] -> convert this to max heap
# until we have 1 or 0 element in the heap, do
    # pop 2 elements
    # if not equal add y-x to the heap
# if 1 remain, return weight else 0
"""
import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapq.heapify(stones)

        while len(stones) >= 2:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)

        if len(stones) == 1:
            return -1 * stones[0]
        return 0
