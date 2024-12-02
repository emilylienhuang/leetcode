class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for i, cite in enumerate(citations):
                if cite >= i + 1:
                    h+=1
        return h
        
