class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        '''
        Need: BFS or DFS
        Keep Teack of: Fresh oranges, rotting oranges ... set? deque?
        rotting_oranges = deque()
        fresh_oranges = set()

        r = rows
        c = cols
        for r in range rows
            for c in range cols
                if grid[r][c] == 1
                    fresh_oranges.add((r,c))
                else:
                    rottine_oranges.append((r,c))
        if not rotting_oranges:
            return -1
        # choose bfs
        while rotting_oranges
            curr_r, curr_c = rotting_oranges.popleft
            for each direction
                if there is an orange
                    make it rot
                    remove from fresh
                    add to rotting oranges
            if rotting oranges
                minutes += 1
        
        if len(fresh) > 0
            return -1
        else
            return minutes
        '''

        rows = len(grid)
        cols = len(grid[0])
        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols

        rotting = deque()
        fresh = set()
        # iterate over the grid. NOTE: this operation costs us O(n) time and O(n) space
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh.add((r,c))
                if grid[r][c] == 2:
                    rotting.append((r,c))
        
        # if there are only fresh oranges on the board its impossible to convert
        if not rotting and fresh:
            return -1
        # if the oranges are all rotten no elapsed time is needed
        if rotting and not fresh:
            return 0
        
        #keep track of elapsed time
        minutes = 0
        # left, right, down, up
        directions = [[1,0], [0,1], [-1, 0], [0,-1]]
        while rotting: # up to O(n) rotting allocation
            for _ in range(len(rotting)):
                cr, cc = rotting.popleft()
                for dr, dc in directions:
                    nr, nc = dr + cr, dc + cc
                    if valid(nr, nc) and grid[nr][nc] == 1:
                        # we need to rot the orange
                        grid[nr][nc] = 2
                        fresh.remove((nr,nc))
                        rotting.append((nr,nc))
            if rotting:
                minutes += 1
            
        if fresh:
            return -1
        return minutes
    