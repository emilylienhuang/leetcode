class Solution:
    def numSquares(self, n: int) -> int:

        perfect_squares = []
        for i in range(n + 1):
            if math.isqrt(i) * math.isqrt(i) == i:
                perfect_squares.append(i)

        if n in perfect_squares:
            return 1

        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(n + 1): 
            for num in perfect_squares:
                dp[i] = min([dp[i], dp[i - num] + 1])
        print(dp)
        return dp[-1]
            