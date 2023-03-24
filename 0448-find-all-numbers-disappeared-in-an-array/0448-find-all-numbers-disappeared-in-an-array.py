class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maxi = max(nums)
        newlist = [0] * len(nums)
        ans = []
        
        for i in range(len(nums)):
            newlist[nums[i]-1] += nums[i]
        
        
        for i in range(len(newlist)):
            if newlist[i] == 0:
                ans.append(i+1)
        return ans