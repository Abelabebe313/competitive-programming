class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
       
        for i in range(0,len(nums)+1):
            if i not in nums:
                return i
                break
            
        return 0