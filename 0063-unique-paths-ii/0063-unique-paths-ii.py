class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # keep track of rows versus columns
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = 1 if obstacleGrid[0][0] != 1 else 0

    
        for r in range(1, rows):
            if obstacleGrid[r][0] == 0:
                dp[r][0] = dp[r - 1][0]
            else:
                dp[r][0] = 0
        
        for c in range(1, cols):
            if obstacleGrid[0][c] == 0:
                dp[0][c] = dp[0][c-1]
            else:
                dp[0][c] = 0

        # iterate over the board and count the unique paths
        for r in range(1, rows):
            for c in range(1, cols):
                left = dp[r][c-1]
                down = dp[r - 1][c]
                if obstacleGrid[r][c] == 0:
                    dp[r][c] = left + down
                else:
                    dp[r][c] = 0
        
        return dp[rows - 1][cols - 1] if dp[rows - 1][cols - 1] > 0 else 0