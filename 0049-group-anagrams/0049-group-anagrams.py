class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_to_anas = {}
        for s in strs:
            word = [0] * 26
            for c in s:
                word[ord(c) - ord('a')] += 1
            
            if tuple(word)not in word_to_anas:
                word_to_anas[tuple(word)] = [s]
            else:
                word_to_anas[tuple(word)].append(s)
        return list(word_to_anas.values())