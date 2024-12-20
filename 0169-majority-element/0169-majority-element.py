class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Moore's algorithm
        # O(1) space
        # O(n) time
        return self.findCandidate(nums)
        
        
        
    def findCandidate(self, nums):
        i_me = 0 # keep track of the index of the majority element
        count = 1 # keep track of the number of occurences
        for i in range(1, len(nums)):
            if nums[i] != nums[i_me]:
                # cancel out one of the majority elements
                count -= 1
            else:
                # increment the majority element count 
                count += 1
            if count == 0:
                i_me = i
                count = 1
        return nums[i_me]