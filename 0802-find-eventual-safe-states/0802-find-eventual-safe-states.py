class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
    
        color = [0] * len(graph)
        # white = 0
        # gray = 1
        # black = 2
        ans = []
        def DFS(node):
            if color[node]==1:
                return False
            if color[node]==2:
                return True
           
            color[node] = 1
            for child in graph[node]:
                if not DFS(child):
                    return False
            color[node] = 2
            ans.append(node)
            return True
                
        for i in range(len(graph)):
            if color[i] != 2:
                DFS(i)
        ans.sort()
        return ans