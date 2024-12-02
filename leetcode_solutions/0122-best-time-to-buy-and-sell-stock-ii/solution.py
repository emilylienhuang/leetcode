class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        maxProf = 0
        for price in prices:
            if price < minPrice:
                minPrice = price
            elif price > minPrice:
                maxProf += price - minPrice
                minPrice = price
        return maxProf
