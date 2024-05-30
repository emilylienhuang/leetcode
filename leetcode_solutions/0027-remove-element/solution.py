class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        p_write = 0
        p_read = 0

        while p_read < len(nums):
            if (nums[p_read] != val):
                nums[p_write] = nums[p_read]
                p_write += 1
            p_read += 1
        return p_write 
