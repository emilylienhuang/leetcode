class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        #rows increasing
        top = 0
        bottom = ROWS - 1
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                bottom = mid - 1
        
        if top >= ROWS:
            return False
        
        left, right = 0, COLS - 1
        row = top
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False