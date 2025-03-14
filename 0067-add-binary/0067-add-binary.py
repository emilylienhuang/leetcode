class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # carry when there is a 1  + 1
        # drop down for a 1 + 0
        # drop down for a 0 + 0

        # reverse indexing a and b
        p_a = len(a) - 1
        p_b = len(b) - 1
        carry = 0 # keep track of 1 + 1's

        ans = []
        while  p_a >= 0 or p_b >= 0 or carry:
            # keep track of my characters
            c_a = a[p_a] if p_a >= 0 else '0'
            c_b = b[p_b] if p_b >= 0 else '0'

            # keep track of what I'm carrying or slot total
            num = int(c_a) + int(c_b) + carry

            if num > 1:
                # case I need to carry something
                ans.append('0')
                carry = 1
            else:
                # case I need to drop the given number
                ans.append(str(num))
                carry = 0
            # reverse iterate strings
            p_a -= 1
            p_b -= 1
        
        # return the string reversed because number was processed reversed
        return ''.join(ans[::-1])

            
