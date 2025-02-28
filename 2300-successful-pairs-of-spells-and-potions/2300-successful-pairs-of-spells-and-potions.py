class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()

        ans = []

        for s in spells:
            min_pot = (success + s - 1) // s
            idx = self.binarySearch(potions, min_pot)
            ans.append(len(potions) - idx)
    
        return ans
    def binarySearch(self, arr, val):
        l, r = 0, len(arr) - 1
        while l <= r:
            m = (l+r)// 2
            if arr[m] < val:
                l = m + 1
            else:
                r = m - 1
        return l