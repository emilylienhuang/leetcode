class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        cols = len(board[0])
        
        def valid(r,c):
            return 0 <= r < rows and 0 <= c < cols

        def dfs_capture(r, c):
            if not valid(r, c) or board[r][c] != "O":
                return 
            
            board[r][c] = "T"
            dfs_capture(r + 1, c)
            dfs_capture(r - 1, c)
            dfs_capture(r, c + 1)
            dfs_capture(r, c - 1)

        # Step 1: Capture the unsurrounded regions 
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r in [0, rows - 1] or c in [0, cols - 1]):
                    dfs_capture(r,c)


        # Step 2: Capture the surrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        # Step 3: Uncapture the unsurrounded regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "T":
                    board[r][c] = "O"