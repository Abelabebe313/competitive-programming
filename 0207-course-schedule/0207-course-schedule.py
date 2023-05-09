class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        incomming = [0] * numCourses
        ans = []
        queue = deque([])
        
        for a,b in prerequisites:
            graph[b].append(a)
            incomming[a] += 1
            
        for idx,count in enumerate(incomming):
            if count == 0:
                queue.append(idx)
        while queue:
            cur_node = queue.popleft()
            ans.append(cur_node)
            for neighbour in graph[cur_node]:
                incomming[neighbour] -= 1
                if incomming[neighbour]==0:
                    queue.append(neighbour)
        if len(ans) != numCourses:
            return False
        return True