class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        letter_freq = collections.defaultdict(int)
        most_occ = 0
        left = 0
        for right, c in enumerate(s):
            letter_freq[c] += 1
            most_occ = max(most_occ, letter_freq[c])
            while (right - left + 1) - most_occ > k:
                letter_freq[s[left]] -= 1
                left += 1
            longest = max(longest, right - left + 1)
        return longest