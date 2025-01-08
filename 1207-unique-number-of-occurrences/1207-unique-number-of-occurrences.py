class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        num_count = Counter(arr)
        for count in num_count.values():
            if count in seen:
                return False
            seen.add(count)
        return True