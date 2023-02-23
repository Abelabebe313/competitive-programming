class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        minn = float('inf')
        summ = 0
        while r < len(nums): 
            # if target > summ:
            summ += nums[r]
            while target <= summ:
                # if r - l == 1:
                #     return 1
                distance = r - l + 1
                minn = min(minn, distance)
                summ -= nums[l]
                l += 1
            r += 1
        if minn == float('inf'):
            return 0
        return minn 