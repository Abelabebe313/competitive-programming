class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        if amount == 0:
            return 0
        def dp(cur):
            if cur == 0:
                return 0
            if cur < 0:
                return float('inf')
            if cur in memo:
                return memo[cur]
            temp = float('inf')
            for j  in range(len(coins)):
                temp = min(temp, dp(cur-coins[j])) 
            memo[cur] = temp + 1
            return memo[cur]

        min_val = dp(amount)

        if min_val == float('inf'):
            return -1
        return min_val