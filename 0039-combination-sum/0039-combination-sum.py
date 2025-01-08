class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = set()

        def backtrack(comb, idx, total):
            if total == target:
                res.add(tuple(comb[:]))
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
        return list(res)