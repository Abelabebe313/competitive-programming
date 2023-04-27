class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        time,fresh = 0,0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i,j))
                    
        def inbound(row,col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        
        while queue and fresh > 0:
            for i in range(len(queue)):
                r,c = queue.popleft()
                for row_change,col_change in direction:
                    new_row = r + row_change
                    new_col = c + col_change
                    
                    if inbound(new_row,new_col) and grid[new_row][new_col]==1:
                        grid[new_row][new_col] = 2
                        queue.append((new_row,new_col))
                        fresh -= 1
            time += 1
           
        if fresh == 0:
            return time
        return -1
                
                   