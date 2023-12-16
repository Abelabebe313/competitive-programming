class Solution:
    def rob(self, nums: List[int]) -> int:
        def robber(house):
            rob1 = 0
            rob2 = 0
            for n in house:
                temp = max(n + rob1,rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        if len(nums) == 1:
            return nums[0]
       
        return  max(robber(nums[1:]),robber(nums[:-1]))