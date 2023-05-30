class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        memo = defaultdict()
        memo[0] = 0
        memo[1] = 1
        maxx = 0
        def maxim(i):
            nonlocal maxx
            if i == 0:
                return 0
            if i == 1:
                return 1
            if i not in memo:
                if i % 2 == 0:
                    memo[i] = maxim(i//2)
                    # maxim((i//2)+1)
                else:
                    memo[i] = maxim(i//2) + maxim((i//2)+1)
            maxx = max(maxx,memo[i])
            
            return memo[i]
        for i in range(n, -1, -1):
            if i not in memo:
                maxim(i)
            else:
                maxx = max(maxx,memo[i])
        return maxx