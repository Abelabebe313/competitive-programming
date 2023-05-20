class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        parent = {i:i for i in range(n)}
        rank = {i:1 for i in range(n)}
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
            rank[x_rep] += y_rep
        
        for i in range(n):
            for j in range(i+1 ,n):
                if len(set(accounts[i]).intersection(accounts[j])) > 1:
                    union(i,j)
                    print(i,j)
        ans = defaultdict(list)
        for idx in range(len(accounts)):
            ans[find(idx)].append(idx)
        
        final_ans = []
        for key, val in ans.items():
            temp = set()
            name = accounts[key][0]
            for i in val:
                temp.update(accounts[i][1:])
            temp = sorted(list(temp))
            temp = [name] + temp
            final_ans.append(temp)
            
        return final_ans
                
            
            
            
            
            
            
                
             