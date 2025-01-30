class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            
            while stack and stack[-1][1] < temp:
                old_i, old_temp = stack.pop()
                ans[old_i] = i - old_i
            stack.append((i, temp))
        return ans
        
            