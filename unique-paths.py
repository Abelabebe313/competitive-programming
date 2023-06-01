class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        def inbound(row,col):
            return (0 <= row < m) and ( 0 <= col < n)

        def dp(row,col):
            if row == m -1 and col == n - 1:
                return 1
            if not inbound(row,col):
                return 0
            state = (row,col)
            if state not in memo:
                memo[state] = dp(row,col+1) + dp(row+1,col)
            return memo[state] 
        return dp(0,0)