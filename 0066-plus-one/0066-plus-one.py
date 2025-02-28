class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        pointer = len(digits) - 1
        while pointer >= 0 and digits[pointer] == 9:
            # we are finding insertion location
            digits[pointer] = 0
            pointer -= 1
        
        # insert because we found the position of pointer
        if pointer < 0:
            digits.insert(0, 1)
        else:
            digits[pointer] += 1
        return digits
        

