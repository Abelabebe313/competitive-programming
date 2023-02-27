class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        suffix = [1] * n
        product = []
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in reversed(range(n-1)):
            print(i)
            suffix[i] = suffix[i+1] * nums[i+1]
        print(prefix)
        return [prefix[i] * suffix[i] for i in range(n)]
            