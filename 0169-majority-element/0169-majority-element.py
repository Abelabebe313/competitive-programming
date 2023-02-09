from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        times = len(nums) // 2
        countNum = Counter(nums)
        
        for num in nums:
            if countNum[num] > times:
                return num
                break
        
        
        