class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        queue = deque()
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        
        def inbound(row,col):
            return row < 0 or col < 0 or row == N or col == N
        
        visited = set()
        def dfs(row,col):
            if (inbound(row,col) or not grid[row][col] or (row,col) in visited):
                return
            visited.add((row,col))
            queue.append([row,col])
            for dr,dc in direction:
                dfs(row + dr, col + dc)
                
        def bfs():
            
            path = 0
            while queue:
                for i in range(len(queue)):
                    r,c = queue.popleft()
                    for dr, dc in direction:
                        row = r + dr
                        col = c + dc

                        if inbound(row,col) or (row,col) in visited:
                            continue
                        if  grid[row][col]:
                            return path
                        queue.append([row,col])
                        visited.add((row,col))
                path += 1
        
        for r in range(N):
            for c in range(N):
                if grid[r][c]:
                    dfs(r,c)
                    return bfs()