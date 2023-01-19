class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        great = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = great
            if temp > great:
                great = temp
        return arr
                
                
        # if len(arr)> 1:
        #     for i in range(len(arr)-1):
        #         greatest = i+1
        #         for j in range(i+1,len(arr)):
        #             if arr[greatest] <= arr[j]:
        #                 greatest = j
        #         arr[i] = arr[greatest]
        #     arr[-1] = -1
        #     return arr
        # else:
        #     arr[-1] = -1
        #     return arr