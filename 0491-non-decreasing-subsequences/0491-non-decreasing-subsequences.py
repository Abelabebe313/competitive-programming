class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()
       
        
        def backtracking(idx,path):
            nonlocal result
            if len(path) >= 2:
                result.add(tuple(path))
            if idx == len(nums):
                return
            
            for i in range(idx,len(nums)):
                if (not path or path[-1] <= nums[i]):
                    path.append(nums[i])
                    backtracking(i+1,path)
                    path.pop()
            return
        backtracking(0,[])
        return result
        