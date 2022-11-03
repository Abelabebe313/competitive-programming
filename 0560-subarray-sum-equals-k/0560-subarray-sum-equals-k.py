class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = 0
        sumDict = {0:1}
        sum = 0
        
        for num in nums:
            sum += num
            if sum - k in sumDict:
                count += sumDict[sum-k]
            if sum in sumDict:
                sumDict[sum] += 1
            else:
                sumDict[sum] = 1
        return count
                