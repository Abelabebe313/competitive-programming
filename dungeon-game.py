class Solution:
    def calculateMinimumHP(self, grid: List[List[int]]) -> int:

        row = len(grid)
        col = len(grid[0])

        dp = [[0 for i in range(col+1)] for j in range(row+1)]
        
        dp[row-1][col-1] = -1*grid[row-1][col-1] if grid[row-1][col-1] <= 0 else 0
        
        for i in range(col-2, -1, -1):
            if grid[row-1][i] <= dp[row-1][i+1]:
                dp[row-1][i] = dp[row-1][i+1] - grid[row-1][i] 
        
        for i in range(row-2, -1, -1):
            if grid[i][col-1] <= dp[i+1][col-1]:
                dp[i][col-1] = dp[i+1][col-1] - grid[i][col-1]
        
        
        for i in range(row-2,-1,-1):
            for j in range(col-2, -1, -1):
                val = 0
                if grid[i][j] < 0 :
                    val = min(dp[i+1][j], dp[i][j+1]) + abs(grid[i][j])
                    dp[i][j] = val
                else:
                     val = grid[i][j] - min(dp[i+1][j], dp[i][j+1])
                    
                     if val >= 0:
                        dp[i][j] = 0
                     else:
                        dp[i][j] = -1*val
               
       
        
        return dp[0][0] + 1