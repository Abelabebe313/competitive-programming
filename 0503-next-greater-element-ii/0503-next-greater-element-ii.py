class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1 for i in range(len(nums))]
        length = len(nums) 
        
        for i in range(length*2):
            if not stack:
                stack.append([i,nums[i % length]])
            if stack and stack[-1][1] < nums[i % length]:
                while stack and stack[-1][1] < nums[i % length]:
                    indx,num = stack.pop()
                    ans[indx % length] = nums[i % length]
                stack.append([i,nums[i % length]])
            else: 
                stack.append([i,nums[i % length]])
                
        return ans