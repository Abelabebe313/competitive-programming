class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        parent = {i:i for i in range(len(s))}
        rank = {i:1 for i in range(len(s))}
        
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
                x_rep,y_rep = y_rep, x_rep
            parent[y_rep] = x_rep
            rank[x_rep] += rank[y_rep]
        
        str_list = list(map(str, s))
        
        for a , b in pairs:
            union(a,b)
        connected = defaultdict(list)
        for i in range(len(s)):
            connected[find(i)].append(i)
        
        ans = [''] * len(s)
        for key, val in connected.items():
            
            picked = []
            for i in val:
                picked.append(s[i])
            picked.sort()
            for i in range(len(val)):
                ans[val[i]] = picked[i]
        return ''.join(ans)
            
            
            
                