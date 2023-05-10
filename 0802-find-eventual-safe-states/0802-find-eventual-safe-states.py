class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_hash = defaultdict(list)
        incomming = [0] * len(graph)
        qu = deque([])
        terminal = []
        
        for idx in range(len(graph)):
            for num in graph[idx]:
                graph_hash[num].append(idx)
            incomming[idx] = len(graph[idx])
            
        for i in range(len(incomming)):
            if incomming[i] == 0:
                qu.append(i)
        
        while qu:
            cur_node = qu.popleft()
            terminal.append(cur_node)
            for nbr in graph_hash[cur_node]:
                incomming[nbr] -= 1
                if incomming[nbr]==0:
                    qu.append(nbr)
        terminal.sort()
        return terminal
        