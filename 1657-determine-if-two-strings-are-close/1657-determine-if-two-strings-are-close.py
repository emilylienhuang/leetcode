class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        w1 = [0] * 26
        w2 = [0] * 26

        for c in word1:
            w1[ord(c) - ord('a')] += 1

        for c in word2:
            w2[ord(c) - ord('a')] += 1

        for i in range(26):
            # can only swap existing characters
            if (w1[i] != 0 and w2[i] == 0) or (w1[i] == 0 and w2[i] != 0):
                return False
        
        w1.sort()
        w2.sort()
        
        for i in range(26):
            if w1[i] != w2[i]:
                # cannot swap one for one existing characters
                return False
        return True
        