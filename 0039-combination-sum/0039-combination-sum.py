class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []

        def backtrack(comb, idx, total):
            if total == target:
                res.append(comb[:])
                return
            if total > target:
                return 
            if idx >= len(candidates):
                return
            
            comb.append(candidates[idx])
            backtrack(comb, idx, total + candidates[idx])
            comb.pop()
            backtrack(comb, idx + 1, total)
            return 
        backtrack([], 0, 0)
        return res