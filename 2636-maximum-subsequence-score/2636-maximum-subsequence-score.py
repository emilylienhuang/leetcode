class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        heap = []
        total = 0
        ans = 0

        for a, b in sorted(zip(nums1, nums2), key= lambda ab: -ab[1]):

            # push onto the heap
            heapq.heappush(heap, a)
            total += a

            if len(heap) > k:
                total -= heapq.heappop(heap)
            
            if len(heap) == k:
                ans = max(ans, total * b)
        return ans