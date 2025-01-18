class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        at_reach = set()
        pac_reach = set()

        def valid(r, c):
            return (0 <= r < rows) and (0 <= c < cols)

        def dfs(r, c, visited, lastHeight):
            if not valid(r, c) or (heights[r][c] < lastHeight) or (r,c) in visited:
                return

            visited.add((r,c))
            dfs(r + 1, c, visited, heights[r][c])
            dfs(r - 1, c, visited, heights[r][c])
            dfs(r, c + 1, visited, heights[r][c])
            dfs(r, c - 1, visited, heights[r][c])
            return
        
        for c in range(cols):
            dfs(0, c, pac_reach, heights[0][c])
            dfs(rows - 1, c, at_reach, heights[rows - 1][c])
        
        for r in range(rows):
            dfs(r, 0, pac_reach, heights[r][0])
            dfs(r, cols - 1, at_reach, heights[r][cols - 1])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r,c) in at_reach and (r, c) in pac_reach:
                    res.append([r,c])
        return res