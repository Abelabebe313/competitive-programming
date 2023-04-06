class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        vrtx = defaultdict(int)
        for i in range(len(edges)):
            vrtx[edges[i][0]]  += 1
            vrtx[edges[i][1]]  += 1
            
        for key,val in vrtx.items():
            if val > 1:
                return key
        