class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        prob = {node: float('-inf') for node in range(n)}
        graph = defaultdict(list)
        prob[start] = -1
        for idx, (a,b) in enumerate(edges):
            graph[a].append((b, succProb[idx] ))
            graph[b].append((a, succProb[idx]))

        visited = set()
        priority_queue = [(-1, start)]

        while priority_queue:
            weight,node =  heappop(priority_queue)

            if node in visited:
                continue
            visited.add(node)

            for nbr,succ_prob in graph[node]:
                distance = abs(weight * succ_prob)
                if distance > prob[nbr]:
                    prob[nbr] = distance
                    heappush(priority_queue,(-distance,nbr))

        
        return prob[end] if prob[end] != float('-inf') else 0