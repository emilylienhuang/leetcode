class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                change = i - coin
                if change >= 0:
                    dp[i] = min(1 + dp[change], dp[i])
        return dp[-1] if dp[-1] != amount + 1 else -1