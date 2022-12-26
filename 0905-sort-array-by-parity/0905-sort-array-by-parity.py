class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = 0
        
        for i in range(len(nums)):
            if nums[right] % 2 != 0:
                right += 1
            elif nums[right] % 2 == 0:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left +=1
                right +=1
        return nums