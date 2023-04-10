class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        diection = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0]*(len(grid[0])) for j in range(len(grid))]
        connected = 0
        
        def inbound(row,col):
            return (0 <= row < len(grid)) and ( 0 <= col < len(grid[0]))
        
        def DFS(row,col,visited):
            visited[row][col] = True
            
            for row_change,col_change in diection:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row,new_col) and not visited[new_row][new_col] and grid[new_row][new_col]=='1':
                    DFS(new_row,new_col,visited)
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1' and not visited[i][j]:
                    DFS(i,j,visited)
                    connected += 1
        return connected