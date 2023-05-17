class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = defaultdict()
        rank = [1] * len(edges)
        ans = [-1,-1]
        
        def find(num):
            if num not in parent:
                parent[num] = num
            elif parent[num] != num:
                parent[num] = find(parent[num])
            return parent[num]
        
        def union(x,y):
            x_root = find(x)
            y_root = find(y)
            
            if x_root != y_root:
                if rank[x_root] >= rank[y_root]:
                    parent[y_root] = x_root
                    rank[x_root] += rank[y_root]
                else:
                    parent[x_root] = y_root
                    rank[y_root] += rank[x_root]
            else:
                ans[0],ans[1] = x+1,y+1
        def connected(x,y):
            return find(x) == find(y)
        
        
        for a,b in edges:
            union(a-1,b-1)
        return ans
            
            
        
        