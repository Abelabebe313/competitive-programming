class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        ans = 0
        while left <= right:
            mid = (left + right)//2
            summ = 0
            for num in nums:
                summ += (ceil(num/mid))
            
            if summ > threshold:
                left = mid + 1
            else:
                ans = mid
                right = mid - 1
           
        return ans
            
            