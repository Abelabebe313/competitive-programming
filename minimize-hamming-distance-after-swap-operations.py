class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        n = len(source)
        parent = {i:i for i in range(n)}
        rank = {i:1 for i in range(n)}

        def find(x):
            if parent[x] == x:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep
        
        def union(x,y):
            rep_x = find(x)
            rep_y = find(y)

            if rank[rep_x] > rank[rep_y]:
                rep_x, rep_y = rep_y, rep_x
            parent[rep_y] = rep_x
            rank[rep_x] += rank[rep_y]
        
        new_src = defaultdict(list)
        
        for a,b in allowedSwaps:
            union(a,b)
        
        for i in range(n):
            new_src[find(i)].append(i)
        
        similar = 0
        for val in new_src.values():
            src = defaultdict(int)
            trg = defaultdict(int)
            for idx in val:
                src[source[idx]] += 1
                trg[target[idx]] += 1
            
            for num,count in src.items():
                similar += min(count,trg[num])
        return len(source) - similar