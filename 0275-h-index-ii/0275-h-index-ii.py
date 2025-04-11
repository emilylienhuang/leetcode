class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 1:
            return min(citations[0], 1)
        l, r = 0, len(citations) - 1
        ans = 0
        while l <= r:
            m = (l + r) // 2
            if citations[m] == (len(citations) - m):
                return citations[m]
            elif citations[m] > (len(citations) - m):
                r = m - 1
            else:
                l = m + 1
        return len(citations) - l