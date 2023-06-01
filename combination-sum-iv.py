class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}
        def dp(idx,cur):
            if cur == target:
                return 1
            if cur > target or idx == len(nums):
                return 0
            if (idx,cur) not in memo:
                memo[(idx,cur)] = dp(0,cur + nums[idx]) + dp(idx+1,cur)
            return memo[(idx,cur)] 
        return dp(0,0)