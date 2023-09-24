class Solution:
    def climbStairs(self, n: int) -> int:
        memo = defaultdict(int)
        
        def dp(i):
            if i == 1 or i == 0:
                return 1
            if i not in memo:
                memo[i] = dp(i-1) + dp(i-2)
            return memo[i]
        return dp(n)