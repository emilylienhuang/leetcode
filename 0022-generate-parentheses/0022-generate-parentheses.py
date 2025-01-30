class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []

        def backtrack(openCount, closeCount):
            if openCount >= n and closeCount >= n:
                res.append(''.join(stack[:]))
                return
            
            if openCount < n:
                stack.append('(')
                backtrack(openCount + 1, closeCount)
                stack.pop()
            
            if closeCount < openCount:
                stack.append(')')
                backtrack(openCount, closeCount + 1)
                stack.pop()
        backtrack(0,0)
        return res