class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        output = [] * len(nums)
        left = 0
        
        for i in range(len(nums)-1):  
            if nums[i]==nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
            else:
                continue
                
        for right in range(len(nums)):
            if nums[right] != 0 and nums[left] != 0:
                left += 1
            elif nums[right] == 0 and nums[left] == 0:
                continue
            elif nums[right]!=0 and nums[left] == 0:
                nums[right],nums[left] = nums[left],nums[right]
                left += 1 
        return nums