class Solution:
    def tribonacci(self, n: int) -> int:
        memo = defaultdict()
        def tribon(i):
            if i == 0:
                return 0
            if i == 1 or i == 2:
                return 1
            if i not in memo:
                memo[i] = tribon(i-1) + tribon(i-2) + tribon(i-3)
            return memo[i]
        return tribon(n)