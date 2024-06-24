class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        first = 0
        second = 0
        i = len(nums) - 1
        ans = []

        while i >= 0:
            subtract = target - nums[i]
            if subtract in nums:
                first = nums.index(subtract)
                if first != i:
                    second = i
                    break
            i -= 1
        
        return [first, second]
