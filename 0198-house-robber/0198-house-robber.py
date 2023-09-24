class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [0] * (len(nums) + 2)
        
        for i in range(len(nums)-1,-1,-1):
            rob = dp[i+2] + nums[i]
            not_rob = dp[i+1]
            dp[i] = max(rob,not_rob)
        return dp[0]
            