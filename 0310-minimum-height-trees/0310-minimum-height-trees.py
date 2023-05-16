class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        deg = [0]*n
        qu = deque()
        visited = set()
        ans = [0] * n
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
            deg[a] += 1
            deg[b] += 1
        
        for i in range(n):
            if deg[i]==1:
                qu.append(i)
                visited.add(i)
       
        
        while qu:
            node = qu.popleft()
            
            for nbr in graph[node]:
                if nbr not in visited:
                    ans[nbr] = ans[node]+1
                deg[nbr] -= 1
                if deg[nbr] == 1:
                        qu.append(nbr)
                        visited.add(nbr)
        res = []
        maxi = max(ans)
        for i in range(n):
            if maxi == ans[i]:
                res.append(i)
        return res
                    
