class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
       
        
        def backtracking(idx,path):
            nonlocal result
            if idx >= len(nums):
                if len(path) > 1:
                    result.add(tuple(path))
                return
            if len(path) > 1:
                result.add(tuple(path))
            
            for i in range(idx,len(nums)):
                if (not path or path[-1] <= nums[i]):
                    path.append(nums[i])
                    backtracking(i+1,path)
                    path.pop()
            
        backtracking(0,[])
        return result
        