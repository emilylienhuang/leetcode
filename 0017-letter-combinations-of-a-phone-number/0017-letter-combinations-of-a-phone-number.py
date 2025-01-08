class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        digits_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno', 
            '7':'pqrs',
            '8':'tuv',
            '9': 'wxyz'
        }

        res = []
        def backtrack(idx, comb):
            if idx >= len(digits):
                string = ''.join(comb[:])
                res.append(string)
                return
            
            for letter in digits_to_letters[digits[idx]]:
                comb.append(letter)
                backtrack(idx + 1, comb)
                comb.pop()
        backtrack(0, [])
        return res

