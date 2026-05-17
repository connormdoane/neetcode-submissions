class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 101
        max_profit = -1
        for i in prices:
            min_price = min(min_price, i)
            max_profit = max(max_profit, i - min_price)
        if max_profit < 0:
            return 0
        return max_profit