from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        papers = len(citations)
        left = 0
        right = len(citations) - 1

        if len(citations) == 0:
            return 0

        while left < right:
            mid = (left + right) // 2
            if citations[mid] == papers - mid:
                return papers - mid
            elif citations[mid] < papers - mid:
                left = mid + 1
            else:
                right = mid

        return min(citations[left], papers - left)