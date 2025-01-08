class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        part = []
        def backtrack(start):
            if start >= len(s):
                res.append(part[:])
                return
            for end in range(start, len(s)):
                if self.isPalindrome(s, start, end):
                    part.append(s[start: end + 1])
                    backtrack(end + 1)
                    part.pop()
        backtrack(0)
        return res
            
    def isPalindrome(self, s, start, end):
        substr = s[start: end + 1]
        return substr[::] == substr[::-1]