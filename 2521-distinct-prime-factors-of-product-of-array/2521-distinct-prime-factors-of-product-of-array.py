class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        
        factors = set()
        def prime_factors(n):
            nonlocal factors
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
                
        for num in nums:
            prime_factors(num)
        return len(factors)