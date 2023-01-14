class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        output = []
        for i in range(len(grid)-2):
            temp = []
            for j in range(len(grid[0])-2):
                k = i + 1
                l = j + 1
                maxLocal = float('-inf')
                for row in range(k-1,k+2):
                    for col in range(l-1,l+2):
                        maxLocal = max(maxLocal,grid[row][col])
                temp.append(maxLocal)
            output.append(temp)
        
        return output
        
                        
                        