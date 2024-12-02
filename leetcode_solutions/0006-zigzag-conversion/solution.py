class Solution:
    def convert(self, s: str, numRows: int) -> str:

        if numRows == 1 or numRows >= len(s):
            return s

        rows = ["" for _ in range(numRows)]
        
        i_row = 0
        direction = -1

        for ch in s:
            rows[i_row] += ch
            if i_row == numRows - 1 or i_row == 0:
                direction = -direction

            i_row += direction
           

        return ''.join(s for s in rows)
