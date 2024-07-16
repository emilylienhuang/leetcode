class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        #edge cases:
        if not pattern:
            return True
        if not s or len(s) == 0:
            return False

        #split string
        words = s.split()

        char_to_word = {}
        word_to_char = {}

        if len(pattern) != len(words):
            return False
        
        for char, word in zip(pattern, words):
            if char in char_to_word and word != char_to_word[char]:
                return False
            if word in word_to_char and char != word_to_char[word]:
                return False
            char_to_word[char] = word
            word_to_char[word] = char

        return True
