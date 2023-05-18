class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        n = len(adjacentPairs)
        graph = defaultdict(list)
        ans = []
        visited = set()
        for a, b in adjacentPairs:
            graph[a].append(b)
            graph[b].append(a)
          
        
        for val in graph:
            if len(graph[val]) == 1:
                ans.append(val)
                visited.add(val)
                break
        
        while n >= len(ans):
            node = ans[-1]
            for child in graph[node]:
                if child not in visited:
                    ans.append(child)
                    visited.add(child)
                    
        return ans