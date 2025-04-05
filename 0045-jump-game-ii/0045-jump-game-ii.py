class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        max_reach = 0
        end_ptr = 0
        n = len(nums)

        for i in range(n-1):
            max_reach = max(max_reach, nums[i] + i)
            if max_reach >= n - 1:
                jumps += 1
                break
            if i == end_ptr:
                jumps += 1
                end_ptr = max_reach
        return jumps