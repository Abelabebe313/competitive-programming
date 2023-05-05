class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        queue = deque()
        queue.append(entrance)
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        visited = set()
        visited.add((entrance[0],entrance[1]))
        def inbound(r,c):
            return (0 <= r < len(maze) and 0 <= c < len(maze[0]))
        def at_border(x, y):
            return x == 0 or y == 0 or x == len(maze) - 1 or y == len(maze[0]) - 1

        path = 0
        while queue:
            for i in range(len(queue)):
                r,c = queue.popleft()
                
                for dr, dc in direction:
                    row,col = dr + r, dc + c
                    
                    if inbound(row,col) and at_border(row,col) and maze[row][col] != '+' and [row,col] != entrance:
                        return path + 1
                    
                    if inbound(row,col) and maze[row][col]=='.' and (row, col) not in visited:
                        visited.add((row,col))
                        queue.append([row,col])
            path += 1
        return -1
                
        