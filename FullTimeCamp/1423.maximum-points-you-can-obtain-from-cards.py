#
# @lc app=leetcode id=1423 lang=python3
#
# [1423] Maximum Points You Can Obtain from Cards
#

# @lc code=start
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        right_sum = sum(cardPoints[n-k:])
        left_sum = 0
        max_points = right_sum

        for i in range(k):
            right_sum -= cardPoints[n-k+i]
            left_sum += cardPoints[i]
            max_points = max(max_points, right_sum + left_sum)
        
        return max_points


# @lc code=end

