class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_element =prices[0]

        for price in prices:
            if min_element > price:
                min_element = price
            else:
                max_profit = max(max_profit, price - min_element)
        return max_profit
