class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        maxi = max(nums)
        newlist = [0] * len(nums)
        ans = 0
        
        for i in range(len(nums)):
            newlist[nums[i]-1] += nums[i]
        
        
        for i in range(len(newlist)):
            if newlist[i] > i + 1:
                ans = i+1
        return ans
        