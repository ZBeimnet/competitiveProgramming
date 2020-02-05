from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # new_cost[0] and new_cost[1] --> base cases
        new_cost = cost

        for i in range(2, len(new_cost)):
            # state transition relation
            new_cost[i] += min(new_cost[i - 1], new_cost[i - 2])

        return min(new_cost[-1], new_cost[-2])