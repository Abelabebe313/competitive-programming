class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        newlist = [0] * len(nums)
        dup = 0
        miss = 0
        
        for i in range(len(nums)):
            newlist[nums[i]-1] += nums[i]
        
        
        for i in range(len(newlist)):
            if newlist[i] > i + 1:
                dup = i+1
            elif newlist[i] == 0:
                miss = i + 1
        return [dup,miss]