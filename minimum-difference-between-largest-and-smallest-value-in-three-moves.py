class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 4:
            return 0
        nums.sort()
        
        mini = float(inf)
        for i in range(1,5):
            # print(nums[n-i] , nums[4-i])   
            mini = min(mini,(nums[n-i]-nums[4-i]))
            
        return mini