class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        close_to_open = {'}': '{', ')': '(', ']': '['}
        stack = []
        for c in s:
            if c in close_to_open.values():
                stack.append(c)
            else:
                if not stack or stack[-1] != close_to_open[c]:
                    return False
                else:
                    stack.pop()
        if stack:
            return False
        return True