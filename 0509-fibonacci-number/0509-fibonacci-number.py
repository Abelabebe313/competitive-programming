class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict(int)
        
        def fib(i):
            if i == 0:
                return 0
            if i == 1:
                return 1
            memo[i] = fib(i-1) + fib(i-2)
            return memo[i]
        return fib(n)