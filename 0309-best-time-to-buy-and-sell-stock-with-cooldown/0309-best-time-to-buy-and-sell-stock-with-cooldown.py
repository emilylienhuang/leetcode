class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = {}

        # buying == boolean, idx == where at in list
        def dfs(idx, buying):

            # return if we are out of bounds
            if idx >= len(prices):
                return 0
            
            if (idx, buying) in dp:
                return dp[(idx, buying)]
            
            cooldown = dfs(idx + 1, buying)

            if buying:
                buy = dfs(idx + 1, not buying) - prices[idx]
                dp[(idx, buying)] =  max(buy, cooldown)
            else:
                # sell
                sell = dfs(idx + 2, not buying) + prices[idx]
                dp[(idx, buying)] =  max(sell, cooldown)
            return dp[(idx, buying)]
        
        ans = dfs(0, True)
        return ans
        