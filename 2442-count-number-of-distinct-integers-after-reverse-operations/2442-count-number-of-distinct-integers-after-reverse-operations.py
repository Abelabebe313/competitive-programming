class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        numSet = set(nums)
        for num in nums:
            revers = "".join(reversed(str(num)))
            numSet.add(int(revers))
        return len(numSet)
            