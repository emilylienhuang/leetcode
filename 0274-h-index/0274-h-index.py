class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # we are looking for the "count" at which the # of papers or array index == array value for number of citations
        # instinct: I want this sorted
        # i want to compare the index to the value in the array
        # where index <=  num_citations --> keep incrementing
        # when index > num_citations --> stick
        if len(citations) == 1:
            # if a paper cited no times, then the answer is 0
            # if it has been cited any times, the answer is 1
            return min(citations[0], 1)
        citations.sort()
        for idx, cite in enumerate(citations):
            if len(citations) - idx <= cite:
                # return my answer, the number of "accounted for" "cited enough times papers"
                return len(citations) - idx
        # if i dont find something:
        # the researcher has published less papers then they have cited
        # the count of papers published is greater than those who have been cited
        return 0