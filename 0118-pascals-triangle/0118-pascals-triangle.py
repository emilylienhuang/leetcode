class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        # dp case: new_nums[i] = old_nums[i-1] + old_nums[i]
        dp = [[1], [1, 1]]
        if numRows == 1:
            return [dp[0]]

        for length in range(2, numRows):
            newArr = [0] * (length + 1)
            newArr[0] = 1
            newArr[-1] = 1
            for j in range(1, len(dp[-1])):
                newArr[j] = dp[-1][j] + dp[-1][j-1]
            dp.append(newArr)
        return dp