import numpy as np
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        output = 0
        column = []
        for i in range(len(grid)):
            temp = []
            r = 0
            for j in range(len(grid[0])):
                
                temp.append(grid[j][i])
            column.append(temp)
        
        for glist in grid:
            for clist in column:
                if glist == clist:
                    output += 1
            
        return output