class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) == 1:
            return nums
        d = collections.defaultdict(int)
        for num in nums:
            d[num] += 1
        
        heap = []
        for num, count in d.items():
            heapq.heappush(heap, (count, num))
            while len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            _, num = heapq.heappop(heap)
            res.append(num)
        return res