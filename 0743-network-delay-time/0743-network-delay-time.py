class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        adj_list = collections.defaultdict(list)
        for s, d, w in times:
            adj_list[s].append((d, w)) # destination node, weight
        
        distances = [float('inf')] * (n + 1)
        distances[0] = 0
        distances[k] = 0
        heap = []
        heapq.heappush(heap, (k, 0))

        while heap:
            node, weight = heapq.heappop(heap)
            if weight > distances[node]:
                continue
            
            for nei, w in adj_list[node]:
                if distances[node] + w < distances[nei]:
                    distances[nei] = distances[node] + w
                    heapq.heappush(heap, (nei, distances[nei]))
        return max(distances) if max(distances) < float('inf') else -1