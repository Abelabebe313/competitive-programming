class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        memo = defaultdict(int)
        ans = 0
        N = len(s)
        for i in range(N):
            for j in range(N-1,i-1,-1):
                if s[i] == s[j]:
                    if i == j:
                        memo[(i,j)] = 1
                    else:
                        memo[(i,j)] = 2
                    if i-1 >=0:
                        memo[(i,j)] += memo[(i-1,j+1)]
                else:
                    memo[(i,j)] = memo[(i,j+1)]
                    if i-1 >=0:
                        memo[(i,j)] = max(memo[(i,j)], memo[(i-1,j)])
                ans = max(ans,memo[(i,j)])
        return ans