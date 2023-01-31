class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        L = 0
        R = 1
        while L < len(nums)-1:
            if R < len(nums) and nums[L] == nums[R]:
                nums.pop(R)
            elif R < len(nums) and nums[L] != nums[R]:
                R += 1
                L += 1
  
        print(nums)
   