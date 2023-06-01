class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dp(idx,cur):
            if cur == amount:
                return 1
            if cur > amount or idx == len(coins):
                return 0
            state = (idx,cur) 
            if state not in memo:
                memo[state] = dp(idx, cur + coins[idx]) + dp(idx + 1, cur)
            return memo[state]
        return dp(0,0)