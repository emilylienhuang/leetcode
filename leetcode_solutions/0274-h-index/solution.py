class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations.sort()
        n = len(citations)

        for i , curr_citation_count in enumerate(citations):
            if n - i <= curr_citation_count:
                return n - i
        
        return 0
