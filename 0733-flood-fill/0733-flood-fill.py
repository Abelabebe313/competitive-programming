class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        direction = [(0,-1),(0,1),(-1,0),(1,0)]
        visited = [[0 for i in range(len(image[0]))] for j in range(len(image))]
        original = image[sr][sc]
        
        def inbound(row,col):
            return (0<= row < len(image)) and (0<=col < len(image[0]))
        
        def DFS(row,col,visited):
            visited[row][col] = True
            # if image[row][col] != color:
            image[row][col] = color
            
            for row_change, col_change in direction:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row,new_col) and not visited[new_row][new_col] and image[new_row][new_col]==original:
                    DFS(new_row,new_col,visited)
        
        DFS(sr,sc,visited)
        return image
                
                
        
        