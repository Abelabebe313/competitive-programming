class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        leftSum = [nums[0]]
        rightSum = [nums[-1]]
        
        for i in range(1,n):
            leftSum.append(leftSum[i-1] + nums[i])
            rightSum.append(rightSum[i-1] + nums[n-i-1])
            
        for j in range(len(nums)):
            if leftSum[j] == rightSum[n-j-1]:
                return j
        return -1
            
        
            