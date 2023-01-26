class Solution(object):
    def pancakeSort(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        def reversing(arr,left,right):
            while left < right:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
                right -= 1
        output = []
        left = 0
        # right = len(arr)-1
        for i in range(len(arr)-1,-1,-1):
            MaxIndex = i
            for j in range(i,-1,-1):
                if arr[j] > arr[MaxIndex]:
                    MaxIndex = j
            if MaxIndex != i:
                # MaxIndex = arr.index(max(arr[:i]))
                reversing(arr,left,MaxIndex)
                reversing(arr,left,i)
                output.append(MaxIndex+1)
            # reverse = arr[:MaxIndex][::-1]
            # arr = reverse + arr[MaxIndex:]
            # reversing(arr,left,right)
                output.append(i+1)
            # right -= 1
           
    
        return output  
         
                        
        