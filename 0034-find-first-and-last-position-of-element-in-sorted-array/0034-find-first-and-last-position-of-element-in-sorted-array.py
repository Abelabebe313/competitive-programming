from bisect import bisect_right
from bisect import bisect_left
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left  = 0
        right = len(nums)-1
        
        if len(nums) != 0 and target in nums:
            
            left = bisect_left(nums,target)
            right = bisect_right(nums,target)-1

            if target == nums[left] and target == nums[right]:
                return [left, right]
        else:
            return [-1,-1]