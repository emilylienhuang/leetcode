class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Problem Understanding: 
        1. we can think of this as a fully connected graph where each node is connected to each other node with a weight of the manhattan distance
        2. We can map the points to each other using an adjacency matrix where each entry is the manhattan distance between the two points
        3. We can select the minimum entries in each row if not already in visited
        '''

        # keep track of the index in the adjacency matrix
        point_to_index = {}
        for i, point in enumerate(points):
            point_to_index[i] = point
        
        # keep track of the manhattan distance in the matrix
        adj_mat = [[float('inf')] * len(points) for _ in range(len(points))]
        
        # iterate over each point to point pair in the adjacency matrix
        for r in range(len(points)):
            for c in range(len(points)):
                if r == c:
                    # manhattan distance between a point and itself is 0
                    continue
                else:
                    # get the x,y of each respective point
                    xr, yr = point_to_index[r]
                    xc, yc = point_to_index[c]
                    m_dist = abs(xr - xc) + abs(yr - yc)
                    adj_mat[r][c] = m_dist
        
        min_dist = 0
        for c in range(1, len(points)):
            min_cost = float('inf')
            for r in range(c - 1, len(points)):
                min_cost = min(min_cost, adj_mat[r][c])
            min_dist += min_cost
        print(min_dist)
        return min_dist
        
        


                
