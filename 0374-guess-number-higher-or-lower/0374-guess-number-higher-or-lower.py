# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        pick = 1
        l, r = 1, n
        while l <= r:
            m = (l + r) // 2
            ans = guess(m)
            if ans == 1:
                l = m + 1
            elif ans == -1:
                r = m - 1
            else:
                pick = m
                break
        return pick
            