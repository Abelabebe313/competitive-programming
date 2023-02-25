class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        summ = 0
        for num in nums:
            summ += num
            prefix.append(summ)
        return prefix