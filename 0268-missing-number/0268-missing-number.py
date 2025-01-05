class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = len(nums)
        res = N
        for i in range(N):
            res ^= i ^ nums[i]
        return res