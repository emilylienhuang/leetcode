class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return 1

        left, right = 0, 0
        seen = set()
        max_len = 0
        while right < len(s):
            while left < right and s[right] in seen:
                seen.remove(s[left])
                left += 1
            max_len = max(right - left + 1, max_len)
            seen.add(s[right])
            right += 1
        return max_len