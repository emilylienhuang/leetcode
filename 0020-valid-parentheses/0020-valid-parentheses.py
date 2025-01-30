class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {"}": "{", "]": "[", ")": "("}
        stack = []
        for c in s:
            if stack:
                if c in close_to_open.values():
                    stack.append(c)
                else:
                    if stack:
                        if close_to_open[c] != stack[-1]:
                            return False
                        stack.pop()
                    else:
                        return False
            else:
                stack.append(c)
        return len(stack) == 0
            