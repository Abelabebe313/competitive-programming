class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}
        N = len(prices)
        def dp(idx,isBuyer):
            if idx == N:
                return 0
            state = (idx,isBuyer)
            if state not in memo:
                if isBuyer:
                    
                    buy_now = dp(idx + 1, False) - prices[idx]
                    buy_next = dp(idx + 1, True)
                    memo[state] = max(buy_now,buy_next)
                else:
                    sell_now = dp(idx + 1, True) + prices[idx] - fee
                    sell_next = dp(idx + 1, False)
                    memo[state] = max(sell_now,sell_next)
            return memo[state]
        return dp(0,True)