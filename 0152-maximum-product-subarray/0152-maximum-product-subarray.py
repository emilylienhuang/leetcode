class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [n for n in nums]

        maxProd = float(-inf)
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1] * nums[i], dp[i])
            maxProd = max(maxProd, dp[i])
        return maxProd


