class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS = len(matrix)
        COLS = len(matrix[0])
        
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == float('inf'):
                    continue
                if matrix[r][c] == 0:
                    matrix[r][c] = float('inf')
                    for j in range(COLS):
                        if matrix[r][j] != 0:
                            matrix[r][j] = float('inf')
                    for i in range(ROWS):
                        if matrix[i][c] != 0:
                            matrix[i][c] = float('inf')
      
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == float('inf'):
                    matrix[r][c] = 0

        