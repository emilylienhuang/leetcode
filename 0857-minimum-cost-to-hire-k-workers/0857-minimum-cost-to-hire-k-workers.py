class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        # we want to choose workers based on their quality and pay them at least their wage as a fraction of the total
        # must get paid minimum wage expectation if we can pay it
        # each worker's pay must be directly proportional to their quality.
        # payoff = wage / quality

        # populate the heap with the ratio of choosing the different workers based on their wage to quality rates
        workers = sorted([(w/q, q) for w, q in zip(wage, quality)])
        heap = []
        total_quality = 0
        min_cost = float('inf')

        for ratio, q in workers:
            heapq.heappush(heap, -q)
            total_quality += q

            while len(heap) > k:
                # subtract the max quality they cost too much
                total_quality += heapq.heappop(heap)
            
            if len(heap) == k:
                min_cost = min(min_cost, total_quality * ratio)
        return min_cost