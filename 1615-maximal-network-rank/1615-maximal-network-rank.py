class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        paths = defaultdict(list)
        for i in range(len(roads)):
            paths[roads[i][0]].append(roads[i][1])
            paths[roads[i][1]].append(roads[i][0])
        
        max_rank = float('-inf')
       
        for i in paths:
            for j in paths:
                if j!=i:
                    if i in paths[j]:
                        rank = len(paths[i] + paths[j]) - 1
                        
                    else:
                        rank = len(paths[i] + paths[j] )
                    max_rank = max(max_rank,rank)
        if len(roads) == 0:
            return 0
        return max_rank
            