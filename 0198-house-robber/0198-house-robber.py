class Solution:
    def rob(self, loot: List[int]) -> int:
        n = len(loot)
        dp = [-1] * (n)
        dp[0] = loot[0]
        dp[1] = max(loot[0], loot[1])
        for i in range(2, n):
            print(dp)
            dp[i] = max(dp[i-2] + loot[i], dp[i-1])
        return dp[-1]
