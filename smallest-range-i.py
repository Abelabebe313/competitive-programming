class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        min_num = min(nums)

        max_l = max_num - k
        max_r = max_num + k

        min_l = min_num - k
        min_r = min_num + k

        if min_r >= max_l:
            return 0
        else:
            return abs(max_l - min_r)