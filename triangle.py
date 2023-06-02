class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        N = len(triangle)
        memo = [[0] * len(triangle[i]) for i in range(N-1)]
        memo.append(triangle[-1])
        
        for i in range(N-2,-1,-1):
            for j in range(len(triangle[i])):
                memo[i][j] = min( memo[i+1][j], memo[i+1][j+1] ) + triangle[i][j]
        return memo[0][0]