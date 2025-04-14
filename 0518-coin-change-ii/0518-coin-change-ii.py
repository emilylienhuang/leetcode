class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:  
            return 1
        
        if amount < min(coins):
            return 0
        
        # the dp array storing the values
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for a in range(1, amount + 1):
                change = a - coin
                if change >= 0:
                    dp[a] += dp[change]
        return dp[-1]