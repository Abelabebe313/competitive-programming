class Solution:
    def fib(self, n: int) -> int:
        # with memory
        memo = {}
        def fibonaci(num):
            if num == 0:
                return 0
            if num == 1:
                return 1
            if num in memo:
                return memo[num]
            memo[num] = fibonaci(num-1) + fibonaci(num-2)
            return memo[num]
        
        return fibonaci(n)
            
        