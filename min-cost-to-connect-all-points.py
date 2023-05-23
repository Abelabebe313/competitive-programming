class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        parent = {i:i for i in range(n)}
        rank = [1] * n

        def find(x):
            if parent[x] == x:
                return x
            rep = find(parent[x])
            parent[x] = rep
            return rep
        def union(x,y):
            rep_x = find(x)
            rep_y = find(y)
            
            if rank[rep_x] > rank[rep_y]:
                rep_x,rep_y = rep_y,rep_x
            parent[rep_y] = rep_x
            rank[rep_x] += rank[rep_y]
          
        connected = []

        for i in range(n):
            a,b = points[i]
            for j in range(i+1,n):
                c,d = points[j]
                dis = abs(a-c) + abs(b-d)
                connected.append((dis,i,j))

        connected.sort(key=lambda x:x[0])
        ans = 0

        # print(connected)
        for dis, a, b in connected:
            if find(a) != find(b):
                union(a,b)
                ans += dis

        return ans