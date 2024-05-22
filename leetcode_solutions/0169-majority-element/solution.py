class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        dict = {}
        times = len(nums)//2
        for value in nums:
            if value not in dict:
                dict[value] = 1
            else:
                dict[value] += 1
            if dict[value] > times:
                return value
        return nums[times]
