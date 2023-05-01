class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)
        
        for i in range(len(bombs)):
            for j in range(len(bombs)):
                if i != j:
                    d = dist(bombs[i][:2],bombs[j][:2])  
                    if d <= bombs[i][2]:
                        graph[i].append(j)
                    
        ans = 1
        
        def DFS(node, visited):
            nonlocal ans
            visited.add(node)
            
         
            ans = max(ans, len(visited))
            for elm in graph[node]:
                if elm not in visited:
                   
                    DFS(elm,visited)
            
            
            
        
        for i in range(len(bombs)):
            if i in graph:
                DFS(i, set())
        return ans
            
                    