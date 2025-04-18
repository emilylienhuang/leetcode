class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # if you can take x, you cannot take x - 1 or x + 1
        # create a counter
        num_count = Counter(nums)

        unique_nums = sorted(list(num_count.keys()))
        if len(unique_nums) == 1:
            return num_count[unique_nums[0]] * unique_nums[0]
        dp = [0] * len(unique_nums)
        dp[0] = num_count[unique_nums[0]] * unique_nums[0]
        if unique_nums[1] != unique_nums[0] + 1:
            dp[1] = dp[0] + (num_count[unique_nums[1]] * unique_nums[1])
        else:
            dp[1] = max(dp[0], num_count[unique_nums[1]] * unique_nums[1])
        for i in range(2, len(unique_nums)):
            curr_points = num_count[unique_nums[i]] * unique_nums[i]
            if unique_nums[i] == (unique_nums[i - 1] + 1):
                dp[i] = max(dp[i-1], (dp[i-2] if i > 1 else 0) + curr_points)
            else:
                dp[i] = dp[i-1] + curr_points
          
        return dp[-1]          