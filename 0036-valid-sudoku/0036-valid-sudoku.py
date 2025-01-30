class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        rows_d = collections.defaultdict(set)
        cols_d = collections.defaultdict(set)
        squares_d = collections.defaultdict(set)

        rows = len(board)
        cols = len(board[0])

        for r in range(rows):
            for c in range(cols):
                if board[r][c].isdigit():
                    if board[r][c] not in rows_d[r]:
                        rows_d[r].add(board[r][c])
                    else:
                        return False
                    if board[r][c] not in cols_d[c]:
                        cols_d[c].add(board[r][c])
                    else:
                        return False
                    if board[r][c] not in squares_d[(r//3,c//3)]:
                        squares_d[(r//3,c//3)].add(board[r][c])
                    else:
                        return False
        return True