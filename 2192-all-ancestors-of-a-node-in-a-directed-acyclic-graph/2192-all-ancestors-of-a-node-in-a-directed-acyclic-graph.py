class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        incomming = [0] * n
        
        for start ,end in edges:
            graph[start].append(end)
            incomming[end] += 1
        
        qu = deque()
        for i in range(len(incomming)):
            if incomming[i] == 0:
                qu.append(i)
        ans = [set() for i in range(n)]
        
        while qu:
            node = qu.popleft()
            
            for nbr in graph[node]:
                ans[nbr].add(node)
                for num in ans[node]:
                    if num not in ans[nbr]:
                        ans[nbr].add(num)
                
                incomming[nbr] -= 1
                if incomming[nbr]==0:
                    qu.append(nbr)
        
        return [sorted(ls) for ls in ans]
            
            