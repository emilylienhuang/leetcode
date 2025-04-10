class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num_to_i = {}
        for i, num in enumerate(nums1):
            num_to_i[num] = i
        stack = []
        res = [-1] *len(nums1)

        for j, num in enumerate(nums2):
            while stack and stack[-1] < num:
                idx = num_to_i[stack.pop()]
                res[idx] = num
            if num in nums1:
                stack.append(num)
        return res