class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_list = collections.defaultdict(list)
        
        for source, target, t in times:
            adj_list[source].append((target, t))

        # note to self: order is neighbor, time
        #start from k
        heap = []
        heapq.heappush(heap, (0, k))
        dist = [float('inf')] * n
        dist[k - 1] = 0
        while heap:
            _, node = heapq.heappop(heap)
            neighbors = adj_list[node]
            for nei, weight in neighbors:
                if dist[node - 1] + weight < dist[nei - 1]:
                    dist[nei - 1] = dist[node - 1] + weight
                    heapq.heappush(heap, (dist[nei - 1], nei))
    
        return max(dist) if max(dist) < float('inf') else -1