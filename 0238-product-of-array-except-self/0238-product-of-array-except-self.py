class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return 0
        ans = [1 for _ in range(len(nums))]

        left_sum = 1
        for i in range(len(nums)):
            ans[i] *= left_sum
            left_sum *= nums[i]
        
        right_sum  = 1
        for i in range(len(nums) - 1, -1, -1):
            ans[i] *= right_sum
            right_sum *= nums[i]
        return ans

