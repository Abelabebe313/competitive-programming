class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, kk: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        for i, j, w in times:
            dist[i-1][j-1] = w

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k-1] + dist[k-1][j])
        # print(dist[k-1])
        return max(dist[kk-1]) if max(dist[kk-1]) != float('inf') else -1