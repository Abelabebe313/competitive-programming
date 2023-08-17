class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        N = len(boxes)
        ans = [0] * N
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if boxes[j] == '1':
                    ans[i] += abs(i-j)
        return ans