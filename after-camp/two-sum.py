class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complementMap = {}
        
        for i,n in enumerate(nums):
            diff = target - n
            if diff in complementMap:
                return [complementMap[diff],i]
            complementMap[n] = i
        return 