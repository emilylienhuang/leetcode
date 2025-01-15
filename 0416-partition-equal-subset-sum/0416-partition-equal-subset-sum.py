class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2

        dp = set([0])

        for i in range(len(nums)):
            newDp = set()
            for total in dp:
                newDp.add(nums[i] + total)
                newDp.add(total)
            dp = newDp
        return (target in dp)