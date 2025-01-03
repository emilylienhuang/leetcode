class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj_mat = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                # O(n^2) time - iterating over each set of node pairs
                # O(n^2) space - each connection filed twice
                x2,y2 = points[j]
                m_dist = abs(x1 - x2) + abs(y1 - y2)
                adj_mat[i].append([m_dist, j])
                adj_mat[j].append([m_dist, i])

        # Now we use prim's algorithm to create an MST
        minHeap = [[0,0]] # cost, node
        visited = set() # check if a node has been visited
        distance = 0
        while len(visited) < N: # O(n) time
            cost, node = heapq.heappop(minHeap) # O(logn)
            if node in visited:
                continue
            distance += cost
            visited.add(node)
            for neighCost, neigh in adj_mat[node]: # O(n)
                if neigh not in visited:
                    heapq.heappush(minHeap, [neighCost, neigh]) # O(log n)
        return distance


