class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        output = []
        currSum = 0
        for num in nums:
            if not num % 2:
                currSum += num
        for querie in queries:
            if nums[querie[1]]%2==0:
                currSum -= nums[querie[1]]
            nums[querie[1]] += querie[0]
            
            if nums[querie[1]]%2==0:
                currSum += nums[querie[1]]         
            output.append(currSum)
        
        return output
        
            
#         for i in range(len(queries)):
#             vali = queries[i][0]
#             indexi = queries[i][1]
            
#             nums[indexi] = nums[indexi] + vali
#             tempSum = 0
#             for j in nums:
                
#                 if j%2 == 0:
#                     tempSum += j
#             output.append(tempSum)
#         return output
                    