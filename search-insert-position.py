class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)-1
        ans = 0
        
        while left <= right:
            mid = (left+right)//2
            
            if target ==  nums[mid]:
                return mid
                # ans = mid
                # break
            elif target > nums[mid]:
                left = mid + 1
                # if target > nums[right]:
                #     ans = right + 1
            else:
                right = mid - 1
                # if target > nums[left]:
                #     ans = left + 1
            
       
        if nums[mid] > target:
            return mid
        return mid + 1