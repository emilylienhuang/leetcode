class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        The plot and points can be thought of as  a fully connected graph
        Use an adj matrix or adj list to store the nodes
        THEN we are looking for a minimum spanning tree
        Approach: Kruskals or Prims?
        Prims does not necessitate set inclusion theory, so it makes the most sense!
        NEED:
        let n be the number of points
        - adj mat/ adj list O(n^2) space 
        - min heap O(n ^ 2) space
        - result variable O(1)

        1. build adj list to store connections and their weights
        2. use prims to use the cheapest connections
        while heap: O(n)
            cost, node = heap pop
            if node already visited
                continue
            add node to visited
            res += node cost
            for neighbor in node's neighbors
            # O(nlogn) heap push + neighbor
                push each neighbor and their weight onto the heap
        O(n^2 log n) time
        Let's implement!
        '''
        N = len(points)
        adj_mat = {i: [] for i in range(N)}
        for i in range(N):
            x1, y1 = points[i]
            for j in range(i + 1, N):
                x2, y2 = points[j]
                m_dist = abs(x1 - x2) + abs(y1 - y2)
                adj_mat[i].append([m_dist, j])
                adj_mat[j].append([m_dist, i])

        
        minHeap = [[0,0]] # cost, point
        res = 0
        visited = set()
        while len(visited) < N:
            cost, point = heapq.heappop(minHeap)
            if point in visited:
                continue
            visited.add(point)
            res += cost
            for neighCost, nei in adj_mat[point]:
                if nei not in visited:
                    heapq.heappush(minHeap, [neighCost, nei])
        return res

            