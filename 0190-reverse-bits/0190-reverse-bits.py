class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            bit_val = (n >> i) & 1 # get if a 1 or a zero
            res = res | bit_val << (31 - i)
        return res