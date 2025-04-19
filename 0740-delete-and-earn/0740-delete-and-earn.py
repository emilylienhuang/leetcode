class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        # methodology: I count how many I can take
        # then I take each unique number in my DP array

        num_count = Counter(nums)
        unique_nums = sorted(list(num_count.keys()))
        dp = [0] * len(unique_nums) # taking each kind of number
        dp[0] = num_count[unique_nums[0]] * unique_nums[0] # take the first and smallest thing initialization

        if len(unique_nums) == 1:
            return dp[0]

        if unique_nums[1] == unique_nums[0] + 1:
            # if they are sequential, choose the best
            dp[1] = max(dp[0], num_count[unique_nums[1]] * unique_nums[1])
        else: 
            dp[1] = dp[0] + num_count[unique_nums[1]] * unique_nums[1]

        for i in range(2, len(unique_nums)):
            # how many points we can take from including the current number
            curr_points = num_count[unique_nums[i]] * unique_nums[i]
            if unique_nums[i] - 1 == unique_nums[i - 1]:
                # if they are sequentially close I can either take the thing directly below me 
                # and directly above me or I can take my thing curr_points
                dp[i] = max(dp[i - 1],dp[i - 2] + curr_points)
            else:
                # I take the thing below me plus my current points
                dp[i] = dp[i-1] + curr_points
        
        return dp[-1]