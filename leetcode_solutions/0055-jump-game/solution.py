class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0 # jump variable
        for i, val in enumerate(nums):
            if i > maxReach:
                return False
            maxReach = max(maxReach, i+val)
        return maxReach >= len(nums) - 1
