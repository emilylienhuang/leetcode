class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def house_rob(arr):
            n = len(arr)
            dp = [-1] * (n)
            dp[0] = arr[0]
            dp[1] = max(arr[1], arr[0])
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + arr[i])
            return dp[n -1]

        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        return max(house_rob(nums[:-1]), house_rob(nums[1:]))