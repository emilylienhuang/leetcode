class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = strs[0]
        for word in strs:
            i = 0
            if word != prefix:
                while i < len(word) and i < len(prefix):
                    if word[i] != prefix[i]:
                        prefix = prefix[0:i]
                        break
                    i+=1
        return prefix

