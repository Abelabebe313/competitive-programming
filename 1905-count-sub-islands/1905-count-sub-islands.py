class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        direction = [(0,1),(0,-1),(1,0),(-1,0)]
        visited = [[0] * len(grid2[0]) for i in range(len(grid2))]
        
        ans = 0
        flag = True
        def inbound(row,col):
            return (0 <= row < len(grid2)) and (0 <= col < len(grid2[0]))
        
        def DFS(row,col):
            nonlocal visited,flag
            visited[row][col] = True
            if grid1[row][col] == 0:
                flag = False
            
            for row_change, col_change in direction:
                new_row = row + row_change
                new_col = col + col_change
                
                if inbound(new_row,new_col) and not visited[new_row][new_col] and grid2[new_row][new_col] == 1:
                    if grid1[new_row][new_col] == 0:
                        flag = False
                    DFS(new_row,new_col)
            return 1 if flag else 0
        
        for i in range(len(grid2)):
            for j in range(len(grid2[0])):
                if grid2[i][j] == 1 and not visited[i][j]:
                    flag = True
                    if DFS(i,j):
                        ans += 1
        return ans
        
        
                    