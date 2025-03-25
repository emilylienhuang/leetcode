class Solution:
    def numSquares(self, n: int) -> int:
        if n == 1:
            return 1
            
        perfect_squares = []
        for i in range(n):
            if math.isqrt(i) * math.isqrt(i) == i:
                perfect_squares.append(i)
        
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1): 
            for num in perfect_squares:
                dp[i] = min(dp[i], dp[i - num] + 1)
        return dp[-1]
            