class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [arr[0]]
        current = 0
        totalSum = 0
        
        for i in range(1,n):
            prefix.append(prefix[i-1] + arr[i])
            
        while len(prefix) > 0:
            for i in range(0,len(prefix),2):
                totalSum += prefix[i] - current
            current  = prefix[0]
            prefix.pop(0)
            
        return totalSum
        