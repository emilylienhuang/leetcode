class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p_write = 1
        occurrences = 1
        for p_read in range(1, len(nums)):
            if (nums[p_read] == nums[p_read -1 ]):
                occurrences += 1
            else:
                occurrences = 1
            if occurrences <= 2:
                nums[p_write] = nums[p_read]
                p_write += 1
        return p_write
                
        
