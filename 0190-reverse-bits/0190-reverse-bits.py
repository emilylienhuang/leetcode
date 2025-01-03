class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
           bit = (n >> i) & 1 # get the i'th bit and and it with 1 to get its value
           res = res  | (bit << (31 - i)) # pipe into res shifting over to the furthest available
        return res
