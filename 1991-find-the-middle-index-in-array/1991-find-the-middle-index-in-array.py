class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        leftmost = [nums[0]]
        rightmost = [nums[-1]]
        
        for i in range(1,len(nums)):
            leftmost.append(leftmost[i-1] + nums[i])
            rightmost.append(rightmost[i-1] + nums[len(nums)-i-1])
        for r in range(len(nums)):
            if leftmost[r] == rightmost[len(nums)-r-1]:
                return r
        return -1