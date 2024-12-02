class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits)-1, 0, -1):
                
                if (i == len(digits) - 1):
                    digits[i] += 1
                    
                if (digits[i] // 10 == 1):
                    digits[i] = 0
                    digits[i-1] += 1
                print(digits)
        if (len(digits) == 1):
            digits[0] += 1
        if (digits[0] // 10 == 1):
            digits[0] = 0
            digits.insert(0, 1)
        return digits
