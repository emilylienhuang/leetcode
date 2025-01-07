class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        def backtrack(idx, subset):
            if idx >= len(nums):
                res.add(tuple(subset[:]))
                return 
            subset.append(nums[idx])
            backtrack(idx + 1, subset)
            subset.pop()
            backtrack(idx + 1, subset)
            return
        backtrack(0, [])
        return list(res)
