class Solution:
    def tribonacci(self, n: int) -> int:
        prev, cur, nxt = 0, 1, 1

        # edge cases
        if n == 0:
            return prev
        elif n == 1:
            return cur
        elif n == 2:
            return nxt

        for i in range(2, n):
            tmp1, tmp2 = cur, nxt
            nxt = prev + cur + nxt
            prev = tmp1
            cur = tmp2
        return nxt