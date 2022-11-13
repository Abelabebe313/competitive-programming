class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        min_n = 0
        sum_n = 0
        
        for i in range(len(nums)):
            sum_n += nums[i]
            min_n = min(min_n,sum_n)
        return 1 - min_n