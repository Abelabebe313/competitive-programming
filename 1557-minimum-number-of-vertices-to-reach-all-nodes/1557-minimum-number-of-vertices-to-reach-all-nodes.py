class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        paths = defaultdict(set)
        dest = set()
        source = set()
        ans = []
        for i in range(len(edges)):
            source.add(edges[i][0])
            dest.add(edges[i][1])
        for i in range(n):
            if i not in dest:
                ans.append(i)
        return ans
        