class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        l, r = 0, len(nums) - 1
        min_elem = float('inf')
        while l <= r:
            m = (l + r) // 2
            if nums[l] <= nums[m]:
                min_elem = min(min_elem, nums[l])
                l = m + 1
            else:
                min_elem = min(nums[m], min_elem)
                r = m - 1
        return min_elem