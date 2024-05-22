class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i_real = 0
        i_curr = 0
        k = 1
        while(i_curr < len(nums)):
            if (nums[i_curr] != nums[i_real]):
                nums[i_real + 1] = nums[i_curr]
                i_real += 1
                k+=1
            i_curr += 1
        return k
            
