class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        
        for i in range(len(edges)):
            graph[edges[i][0]].append(edges[i][1])
            graph[edges[i][1]].append(edges[i][0])

        visited = set()
        def dfs(vertx , visited):
            # base case
            
            if vertx == destination:
                return True
            visited.add(vertx)
            for neghbor in graph[vertx]:
                if neghbor not in visited:
                    found = dfs(neghbor,visited)
                    if found:
                        return True
        return dfs(source,visited)