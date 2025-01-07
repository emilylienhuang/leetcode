class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(idx, comb):
            if idx >= len(nums):
                res.append(comb[:])
                return

            comb.append(nums[idx])
            backtrack(idx + 1, comb)
            comb.pop()
            backtrack(idx + 1, comb)
        backtrack(0, [])

        return res