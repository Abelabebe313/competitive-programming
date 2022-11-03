class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        leftSum = []
        rightSum = []
        
        for i in range(len(nums)):
            
            if(i):
                leftSum.append(leftSum[i-1] + nums[i])
                rightSum.append(rightSum[i-1] + nums[len(nums)-i-1])
            else:
                leftSum.append(nums[i])
                rightSum.append(nums[len(nums)-1])
        for i in range(len(nums)):
            if leftSum[i] == rightSum[len(nums)-i-1]:
                return i
        return -1
                