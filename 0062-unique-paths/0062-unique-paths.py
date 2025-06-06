class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        dp = [[0] * (n) for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                top_down = dp[i-1][j]
                left_right = dp[i][j-1]
                dp[i][j] += top_down + left_right
        
        return dp[m-1][n-1]