from collections import Counter
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        numCount = Counter(nums)
        
        for num in nums:
            if numCount[num] > 1:
                return True
        return False
            