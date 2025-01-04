class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        def get_next_num(number):
            output = 0
            while number:
                digit = number % 10
                output += digit ** 2
                number = number // 10
            return output
        
        while n not in visit:
            visit.add(n)
            n = get_next_num(n)
            if n == 1:
                return True
        return False