class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, search_left):
            idx = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                m = l + (r - l) // 2
                if nums[m] < target:
                    l = m + 1
                elif nums[m] > target:
                    r = m - 1
                else:
                    idx = m
                    if search_left:
                        r = m - 1
                    else:
                        l = m + 1
            return idx
        
        left = binary_search(nums, target, True)
        right = binary_search(nums, target, False)
        return [left, right]

        