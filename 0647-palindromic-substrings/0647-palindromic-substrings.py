class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            left, right = i, i
            res += self.isPali(s, left, right)
            left,right = i, i + 1
            res += self.isPali(s, left, right)
        return res
    def isPali(self, s, left, right):
        res = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            res += 1
            left -= 1
            right += 1
        return res