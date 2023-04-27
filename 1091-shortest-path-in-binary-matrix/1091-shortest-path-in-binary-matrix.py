class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        direction = [[0,1],[1,0],[0,-1],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1]]
        n = len(grid)
        queue = deque([(0,0)]) if grid[0][0] == 0 else deque()
        visited = set()
        visited.add((0,0))
        
        def inbound(row,col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))
        path = 0
        
        while queue:
            length = len(queue)
            path += 1            
            for i in range(length):
                r,c = queue.popleft()
                if r == n-1 and c == n-1:
                    return path
                for dr,dc in direction:
                    row,col = r + dr, c + dc
                    if inbound(row,col) and grid[row][col]==0 and (row,col) not in visited:
                        queue.append((row,col))
                        visited.add((row,col))
            
        return -1