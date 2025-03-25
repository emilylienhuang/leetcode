class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # use a top-down approach with padding the top row and first col
        rows = len(grid)
        cols = len(grid[0])

        dp = [[0] * cols for _ in range(rows)]
        dp[0][0] = grid[0][0]

        # pad row => going right
        for r in range(1, rows):
            dp[r][0] = dp[r - 1][0] + grid[r][0]

        # pad col => going down
        for c in range(1, cols):
            dp[0][c] = dp[0][c - 1] + grid[0][c]
        
        for r in range(1, rows):
            for c in range(1, cols):
                #must pay the cost of movement from the prior path
                dp[r][c] = min(dp[r - 1][c], dp[r][c - 1]) + grid[r][c]
        
        return dp[rows - 1][cols - 1]
