from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x: x[0] - x[1])
        minimum_cost = 0

        for i in range(len(costs)):
            if i < (len(costs) // 2):
                minimum_cost += costs[i][0]
            else:
                minimum_cost += costs[i][1]

        return minimum_cost