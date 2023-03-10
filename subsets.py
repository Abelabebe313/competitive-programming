class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def traverse(idx,lst):
            if len(lst) == len(nums):
                ans.append(lst)
                return
            ans.append(lst)
            for i in range(idx,len(nums)):
                traverse(i+1,lst+[nums[i]])

        traverse(0,[])
        return ans