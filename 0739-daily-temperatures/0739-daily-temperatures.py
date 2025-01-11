class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n =  len(temperatures)
        ans = [0] * n

        stack = []
        for i, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                # we found a warmer day
                old_i, old_temp = stack.pop()
                ans[old_i] = i - old_i
            if not stack or stack[-1][1] >= temp:
                stack.append([i, temp])
        return ans
