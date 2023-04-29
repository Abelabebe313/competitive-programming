class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        queue = deque()
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        def inbound(row,col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))
        
        ans = [[0] * len(mat[0]) for i in range(len(mat))]
        level = 0
        while queue:
            length = len(queue)
            level += 1
            for i in range(length):
                r,c = queue.popleft()
                
                for dr,dc in direction:
                    row = r + dr
                    col = c + dc
                    
                    if inbound(row,col) and (row,col) not in visited and mat[row][col] == 1:
                        queue.append((row,col))
                        ans[row][col] = level
                        visited.add((row,col))
        return ans
                    
                 
        
        
                