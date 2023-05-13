class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        ans = [-1] * len(quiet)
        graph = defaultdict(list)
        
        for a,b in richer:
            graph[b].append(a)
        print(graph)
        def DFS(node):
            if ans[node] == -1:
                ans[node] = node
                for child in graph[node]:
                    mini = DFS(child)
                    if quiet[mini] < quiet[ans[node]]:
                        ans[node] = mini
            return ans[node]
                        
                        
        for i in range(len(quiet)):
            DFS(i)
        return ans
            