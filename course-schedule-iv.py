class Solution(object):
    def checkIfPrerequisite(self, numCourses, prerequisites, queries):
        n = numCourses
        dist = [[False] * n for _ in range(n)]
        for i, j in prerequisites:
            dist[i][j] = True

        for i in range(n):
            dist[i][i] = True

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = dist[i][j] or (dist[i][k] and dist[k][j])
        ans = []
        for u,v in queries:
            ans.append(dist[u][v])
        return ans