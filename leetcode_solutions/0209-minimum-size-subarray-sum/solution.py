class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left_ptr = 0
        curr_sum = 0
        min_length = float('inf')

        for right_ptr in range(n):
            curr_sum += nums[right_ptr]
            while curr_sum >= target:
                min_length = min(min_length, right_ptr - left_ptr + 1)
                curr_sum -= nums[left_ptr]
                left_ptr += 1

        return min_length if min_length != float('inf') else 0
