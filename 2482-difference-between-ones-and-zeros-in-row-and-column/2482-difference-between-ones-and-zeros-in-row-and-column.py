class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        diff = [[0 for i in range(len(grid[0]))] for i in range(len(grid))]
        m = len(grid)
        sumRow = []
        sumCol = []
        for i in range(m):
            temp = 0
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    temp -= 1
                else:
                    temp += 1
            sumRow.append(temp)
            
        for i in range(len(grid[0])):
            temp = 0
            for j in range(len(grid)):
                if grid[j][i] == 0:
                    temp -= 1
                else:
                    temp += 1
            sumCol.append(temp)
        
        for i in range(len(sumRow)):
            for j in range(len(sumCol)):
                diff[i][j] = sumRow[i] + sumCol[j]
        return diff
        