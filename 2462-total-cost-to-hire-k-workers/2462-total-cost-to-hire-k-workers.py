class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        l, r = 0, len(costs) - 1
        heap1 = []
        heap2 = []

        total_cost = 0
        while k > 0:
            while len(heap1) < candidates and l <= r:
                heapq.heappush(heap1, costs[l])
                l += 1
            
            while len(heap2) < candidates and l <= r:
                heapq.heappush(heap2, costs[r])
                r -= 1
            
            top1 = heap1[0] if heap1 else float('inf')
            top2 = heap2[0] if heap2 else float('inf')

            if top1 <= top2:
                total_cost += top1
                _ = heapq.heappop(heap1)
            else:
                total_cost += top2
                _ = heapq.heappop(heap2)
            k -= 1
        return total_cost