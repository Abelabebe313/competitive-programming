class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = 0
        for i in range(len(nums)):
            if nums[right] == 0 and nums[left]==0:
                right += 1
            elif nums[right] != 0 and nums[left]==0:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1
                right += 1
            elif nums[right] != 0 and nums[left] != 0:
                left += 1
                right += 1