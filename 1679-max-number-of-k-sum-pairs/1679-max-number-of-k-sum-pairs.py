class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        op = 0
        for i in count:
            op += min(count[i],count[k-i])
        return op//2