class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        l, r = 1, max(piles) #  = [1, 2, 3, ..... , max(piles)]
        optimal_k = max(piles)
        while l <= r:
            k = (l + r)//2
            hours = 0
            for pile in piles:
                hours += math.ceil(float(pile) / k)
            if hours <= h:
                optimal_k = min(optimal_k, k)
                r = k - 1
            else:
                # need to eat more bananas
                l = k + 1
        return optimal_k
