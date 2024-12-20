from collections import defaultdict
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_occ = collections.defaultdict(int)
        for num in nums:
            num_occ[num] += 1

        ans = []
        for num, occ in num_occ.items():
            if occ > len(nums) // 3:
                ans.append(num)
        return ans