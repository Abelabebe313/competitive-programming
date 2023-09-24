class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = defaultdict()
        
        def dp(i):
            if i >= len(nums):
                return 0
            if i not in memo:
                rob = dp(i+2) + nums[i]
                not_rob = dp(i+1)
                memo[i] = max(rob,not_rob)
            return memo[i]
        return dp(0)
            