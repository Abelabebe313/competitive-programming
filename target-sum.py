class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        ans = 0
        memo = {}
        def dp(idx,total):
            if idx == N:
                if total == target:
                    return 1
                else:
                    return 0
                    
            if (idx,total) in memo:
                return memo[(idx,total)]
            postive = dp(idx + 1, total + nums[idx])
            negative = dp(idx + 1, total - nums[idx])
            
            memo[(idx,total)] =  postive + negative

            return memo[(idx,total)]

        return dp(0,0)