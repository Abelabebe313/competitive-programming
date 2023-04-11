class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        conn_dict = defaultdict(list)
        
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1 and i!=j:
                    conn_dict[i+1].append(j+1)
        # print(conn_dict)
        count = 0
        visited = set()
        def DFS(ID):
            nonlocal visited
            visited.add(ID)
            for child in conn_dict[ID]:
                if child not in visited:
                    DFS(child)
            
        for i in range(1,len(isConnected)+1):
            if i not in visited:
                DFS(i)
                count += 1
                
        return count