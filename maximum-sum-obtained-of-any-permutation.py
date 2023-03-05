class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        lineSweep = [0] * ((len(nums)) + 1)
        
        for start,end in requests:
            lineSweep[start] += 1
            lineSweep[end + 1] -= 1
        prefix = []
        summ = 0
        for i in lineSweep:
            summ += i
            prefix.append(summ)
        prefix.pop()
        
        nums.sort()
        prefix.sort()
        print(nums, prefix)
        ans = 0
        for i in range(len(nums)):
            ans += nums[i] * prefix[i]
        return ans%((10**9)+7)