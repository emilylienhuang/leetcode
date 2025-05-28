class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l_ptr = 0
        curr_sum = 0
        min_length = float('inf')

        for r_ptr in range(n):
            curr_sum += nums[r_ptr]
            while curr_sum >= target:
                min_length = min(min_length, r_ptr - l_ptr + 1)
                curr_sum -= nums[l_ptr]
                l_ptr += 1
        
        return min_length if min_length != float('inf') else 0