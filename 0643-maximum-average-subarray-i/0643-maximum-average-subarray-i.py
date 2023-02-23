class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # maxSub = float(-inf)
        # count = 0
        # avg = 0
        # l = 0
        # for r in range(len(nums)):
        #     count += nums[r]
        #     if r >= k:
        #         count -= nums[l]
        #         l += 1
        #     if r >= k - 1:
        #         avg = count/k
        #         maxSub = max(avg,maxSub)
        # return maxSub
        
        
        sums = sum(nums[:k])
        maxi = sums / k
        for i in range(len(nums) - k):
            sums += nums[k + i]
            sums -= nums[i]
            avg = sums/k
            # sums /= k
            maxi = max(avg,maxi)
        return maxi
            
            
                  