class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        max_reach = 0
        for i in range(len(nums) - 1):
            if i > max_reach:
                return False
            max_reach = max(nums[i] + i, max_reach)
            
        
        return max_reach >= len(nums) -1 