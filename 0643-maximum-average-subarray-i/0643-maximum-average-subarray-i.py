class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxSub = float(-inf)
        count = 0
        avg = 0
        l = 0
        for r in range(len(nums)):
            count += nums[r]
            if r >= k:
                count -= nums[l]
                l += 1
            avg = count/k

            if r >= k - 1:
                maxSub = max(avg,maxSub)
        return maxSub