class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def dfs(idx, total):
            if (idx, total) in dp:
                return dp[(idx, total)]
            
            if idx == len(nums):
                return total == target
            
            add = dfs(idx + 1, total + nums[idx])
            subtract = dfs(idx + 1, total - nums[idx])
            dp[(idx, total)] = add + subtract
            return dp[(idx, total)]
        
        return dfs(0, 0)