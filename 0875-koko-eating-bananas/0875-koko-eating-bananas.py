class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        '''
        edge cases: only one pile
        min_num_bananas (l), max_num_bananas(r)
        time = 0
        while l <= r:
            k = l + r // 2
            hours = 0
            for pile in piles:
                hours += chomp down on pile
            if hours <= h:
                time = min(hours, time)
                r = k - 1
            else:
                # we need to eat more bananas
                l = k + 1
        '''

        l, r = 1, max(piles)
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
