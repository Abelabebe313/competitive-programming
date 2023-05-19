from typing import List


from typing import List
from collections import *

class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]) -> int:
        # code here
        graph = defaultdict(list)
        indeg = defaultdict(int)
        
        for  i in range(n):
            indeg[i+1] = 0
        
        for u,v in edges:
            graph[u].append(v)
            indeg[v] += 1
        
        qu = deque()
        for key,val in indeg.items():
            if val == 0:
                qu.append([key,1])
                
        times = [0]*n
        while qu:
            node,time = qu.popleft()
            times[node-1] = time
            for nbr in graph[node]:
                indeg[nbr] -= 1
                if indeg[nbr]==0:
                    qu.append([nbr,time+1])
        return ' '.join(map(str,times))
                



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        print(res)
        

# } Driver Code Ends