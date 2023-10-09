class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)
        for (a,b), value in zip(equations,values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        # print(graph)

        def dfs(start,end,visited):
            if start not in graph or end not in graph:
                    return -1.0
            if start == end:
                return 1.0
            visited.add(start)
            for nbr in graph[start]:
                if nbr not in visited:
                    result = dfs(nbr,end,visited)
                    if result != -1.0:
                        return result * graph[start][nbr]
            return -1.0
        ans = []
        for query in queries:
            start,end = query
            visited = set()
            result = dfs(start,end,visited)
            ans.append(result)
        return ans