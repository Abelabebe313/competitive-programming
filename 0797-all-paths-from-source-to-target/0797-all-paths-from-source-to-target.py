class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        target = n - 1
        output = []
        dfs_graph = defaultdict(list)
        for i in range(len(graph)-1):
            dfs_graph[i] = graph[i]
        
        def DFS(node,path):
            nonlocal output
            if node == target:
                path.append(node)
                output.append(path[::])
                return
            
            path.append(node)
            for child in dfs_graph[node]:
                DFS(child,path)
                path.pop()
        DFS(0,[])
        return output