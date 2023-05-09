class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        incomming = defaultdict(int)
        
        for idx,rec in enumerate(recipes):
            for i,ing in enumerate(ingredients[idx]):
                graph[ing].append(rec)
            
            incomming[rec] = len(ingredients[idx])
              
        qu = deque([])
        
        for val in supplies:
            if incomming[val] == 0:
                qu.append(val)
        order = []
        while qu:
            cur_node = qu.popleft()
            if cur_node in recipes:
                order.append(cur_node)
            
            for nbr in graph[cur_node]:
                incomming[nbr]-=1
                if incomming[nbr]==0:
                    qu.append(nbr)
        return order
            
        
    