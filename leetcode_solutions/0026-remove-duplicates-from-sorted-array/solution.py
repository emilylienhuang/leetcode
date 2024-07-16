class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write, read = 0, 1
        while read < len(nums):
            if nums[read] != nums[write]:
                write += 1
                nums[write] = nums[read]
            read += 1
        return write + 1
