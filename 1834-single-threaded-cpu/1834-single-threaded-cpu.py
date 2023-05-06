class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i , task in enumerate(tasks):
            task.append(i)
            
        tasks = sorted(tasks,key=lambda x:x[0])
        
        heap = []
        ans = []
        i = 0
        time = tasks[0][0]
        
        while i < len(tasks) or heap:
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(heap,(tasks[i][1],tasks[i][2]))
                i += 1
            else:
                if heap:
                    process, idx = heapq.heappop(heap)
                    time += process
                    ans.append(idx)
                else:
                    time = tasks[i][0]
        
        return ans       
                
            
        