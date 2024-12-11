class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        res = [False] * len(candies)

        for i, kid in enumerate(candies):
            if kid + extraCandies >= max(candies):
                res[i] = True
        return res