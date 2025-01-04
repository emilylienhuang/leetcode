class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # O(n) space allocation to save the keyboard
        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []
        def backtrack(comb, idx):
            if len(comb) == len(digits):
                res.append(comb[:])
                return
            if idx >= len(digits):
                return

            for letter in digits_to_letters[digits[idx]]:
                backtrack(comb + letter, idx + 1)
            return
        backtrack("", 0)
        return res