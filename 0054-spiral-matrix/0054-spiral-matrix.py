class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = len(matrix[0])
        N = len(matrix)
        left, right = 0, M
        top, bottom = 0, N

        res = []
        while left < right and top < bottom:
            # left to right over outer square
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # down the right-most column
            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            # edge case for no right to left traversal needs
            if not (left < right and top < bottom):
                break


            # shrink the bottom window and go right to left
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])

            # if we went right to left we need to go bottom up til we hit new top
            bottom -= 1
            for i in range(bottom - 1, top - 1, -1 ):
                res.append(matrix[i][left])
            
            left += 1
        
        return res