class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        read, write = 0, 0
        while read < len(nums):
            if nums[read] != val:
                nums[write] = nums[read]
                write += 1
            read += 1
        return write 