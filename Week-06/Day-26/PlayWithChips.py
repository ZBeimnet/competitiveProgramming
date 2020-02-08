class Solution:
    def minCostToMoveChips(self, chips: List[int]) -> int:
        no_odd = no_even = 0

        for i in chips:
            if i % 2 == 0:
                no_even += 1
            else:
                no_odd += 1

        return no_even if no_odd > no_even else no_odd


