class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        
        subsum = sum(nums) // 2
        dp = set()
        dp.add(0)

        for i in range(len(nums)):
            newDp = set()
            for t in dp:
                newDp.add(t + nums[i])
                newDp.add(t)
            dp = newDp
        return (subsum in dp)
                