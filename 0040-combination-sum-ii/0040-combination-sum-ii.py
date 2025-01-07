class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()
        def backtrack(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return 
            if total > target:
                return 
            if idx >= len(candidates):
                return 
            
            comb.append(candidates[idx])
            backtrack(idx + 1, comb, total + candidates[idx])
            comb.pop()

            while idx + 1 < len(candidates) and candidates[idx] == candidates[idx + 1]:
                idx += 1
            backtrack(idx + 1, comb, total)
        backtrack(0, [], 0)
        return list(res)