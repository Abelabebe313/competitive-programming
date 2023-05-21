class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        parent = {i:i for i in range(1,n+1) }
        rank = {i:1 for i in range(1,n+1) }
        
        def find(x):
            if parent[x] == x:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep
        
        def union(x,y):
            x_rep = find(x)
            y_rep = find(y)
            
            if rank[x_rep] > rank[y_rep]:
                x_rep,y_rep = y_rep,x_rep
            parent[y_rep] = x_rep
            rank[x_rep] += rank[y_rep]
            
        # roads.sort(key=lambda x:x[2])
        mini_score = float('inf')
        
        for road in roads:
            source, destination, distance = road
            union(source,destination)
            
        for road in roads:
            source, destination, distance = road
            if find(1) == find(source):
                mini_score = min(mini_score,distance)
                # union(source,destination)
            
        return mini_score