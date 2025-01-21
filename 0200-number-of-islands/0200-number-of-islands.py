class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        seen = set()
        def valid(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs(r,c):
            if valid(r,c) and (r,c) not in seen and grid[r][c] == '1':
                seen.add((r,c))
                dfs(r + 1, c)
                dfs(r, c + 1)
                dfs(r -1, c)
                dfs(r, c-1)
            else:
                return
        
        # Time: O(mn)
        # Space: O(mn)
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in seen and grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)
        return islands