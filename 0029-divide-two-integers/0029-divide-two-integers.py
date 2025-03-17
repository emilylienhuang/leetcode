class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor: 
            return 1
        
        if dividend == -2**31 and divisor == -1:
            return (2**31) - 1
        
        if divisor == 1:
            return dividend
        elif divisor == -1:
            return -dividend
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        n, d = abs(dividend), abs(divisor)
        ans = 0

        while n >= d:
            p = 0
            while n >= (d << p):
                # find the bit to remove
                p += 1
            
            #remove closest to the highest power of 2 you can chunk out
            p -= 1
            n -= (d << p)

            # took "p" pieces of the divisor out
            ans += (1 << p)
        
        if ans > -2 ** 31 and ans < 2**31 -1:
            if sign == -1:
                return -ans
            else:
                return ans
