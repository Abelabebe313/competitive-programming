class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {chr(i+97):chr(i+97) for i in range(26)}
        rank = {chr(i+97):1 for i in range(26)}
        
        def find(x):
            if parent[x]==x:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep
        def union(x,y):
            rep_x = find(x)
            rep_y = find(y)
            
            if rank[rep_x] > rank[rep_y]:
                rep_x,rep_y = rep_y,rep_x
            parent[rep_y] = rep_x
            rank[rep_x] += rank[rep_y]
            
        for a,diff,sign,b in equations:
            if diff == '=':
                union(a,b)
        for a,diff,sign,b in equations:
            if diff == '!':
                if a!=b and find(a) == find(b):
                    return False
                elif a==b:
                    return False
        return True
                