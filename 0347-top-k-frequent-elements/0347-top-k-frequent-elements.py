class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_elems = {}
        for num in nums:
            if num in unique_elems:
                unique_elems[num] += 1
            else:
                unique_elems[num] = 1
        
        heap = []
        for key, val in unique_elems.items():
            heapq.heappush(heap, (-val, key))
        
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans