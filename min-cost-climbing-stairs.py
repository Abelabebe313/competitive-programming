class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict()

        def costCal(n):
            if n == 0 or n == 1:
                return 0
            if n not in memo:
                memo[n] = min(cost[n-1] + costCal(n-1) , cost[n-2] + costCal(n-2) )
            return memo[n]

        return costCal(len(cost))