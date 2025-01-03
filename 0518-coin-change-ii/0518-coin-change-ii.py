class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        '''
        This is a DP algorithm checking each way you can make change based on a given amount of coins
        dp[0] = 0
        iterate up to n using i
            for coin in coins
                if dp[i] == coin : dp[i] += 1
                dp[i]  += dp[coin - i]

        '''
        dp = [0] * (amount + 1) # account for zero based indexing
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i-coin]
        return dp[-1]