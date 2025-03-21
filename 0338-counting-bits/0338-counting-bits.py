class Solution:
    def countBits(self, n: int) -> List[int]:
        
        dp = [0] * (n + 1)
        bit_mask = 1
        for i in range(1, n + 1):
            if bit_mask * 2 == i:
                bit_mask = i
            
            dp[i] = 1 + dp[i - bit_mask]
        return dp