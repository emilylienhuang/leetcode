class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows = len(maze)
        cols = len(maze[0])

        def valid(r, c):
            return 0 <= r < rows and 0 <= c < cols 

        
        directions = [[1,0], [0, 1], [-1, 0], [0, -1]]
        
        q = deque()
        q.append(entrance)
        steps = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if (r, c) in visited:
                    continue

                if [r,c] != entrance and ((0 == r or rows - 1 == r) or (0 == c or cols - 1 == c)):
                    return steps
                
                visited.add((r,c))
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if valid(nr, nc) and maze[nr][nc] != '+':
                        q.append((nr, nc))
            if q:
                steps += 1
            else:
                return -1
        
            

