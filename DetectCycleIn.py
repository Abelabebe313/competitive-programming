from typing import List
class Solution:
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        #Code here
        
        color = [0] * V
        def DFS(node,prev):
            if color[node]==1:
                return False
            if color[node]==2:
                return True
                
            color[node] =  1
            for child in adj[node]:
                if child != prev:
                    if not DFS(child,node):
                        return False
                    
            color[node] = 2
            return True
            
        
        for i in range(V):
            if not DFS(i,-1):
                return True
        
        return False



#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends