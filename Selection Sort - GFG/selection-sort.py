#User function Template for python3

class Solution:
    def selectionSort(self, arr,n):
        n = len(arr)
        
        for i in range(0, n):
            min_value = i
            for j in range(i+1, len(arr)):
                if arr[min_value] > arr[j]:
                    min_value = j
            arr[min_value], arr[i] = arr[i], arr[min_value]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends