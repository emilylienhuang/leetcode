class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]
        if rowIndex == 0:
            return row
        
        for _ in range(rowIndex):
            ans = [1] *(len(row) + 1)
            for i in range(1, len(row)):
                ans[i] = row[i - 1] + row[i]
            row = ans
        return row 
