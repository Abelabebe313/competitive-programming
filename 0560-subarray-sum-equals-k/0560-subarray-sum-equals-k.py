class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        sumDict = {0:1}
        count = 0
        prefix = []
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            prefix.append(sum)
    
        for i in range(len(prefix)):
            if prefix[i] - k in sumDict:
                count += sumDict[prefix[i] - k]
            if prefix[i] in sumDict:
                sumDict[prefix[i]] += 1
            else:
                sumDict[prefix[i]] = 1
        return count
                
                