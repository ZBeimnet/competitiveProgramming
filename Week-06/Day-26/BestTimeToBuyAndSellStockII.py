# buy = False, 3
# max_profit = 4 + 3
# [7,1,5,3,6,4]
# time - O(n)
# space - O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        buy = [False, 0]
        max_profit = 0

        for i in range(length - 1):
            if prices[i] < prices[i + 1] and not buy[0]:
                buy[0] = True
                buy[1] = i
            elif prices[i] > prices[i + 1] and buy[0]:
                buy[0] = False
                max_profit += prices[i] - prices[buy[1]]

        if buy[0]:
            max_profit += prices[length - 1] - prices[buy[1]]
            buy[0] = False

        return max_profit
