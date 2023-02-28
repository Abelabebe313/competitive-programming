class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 1:
            return True
        if n < 1:
            return False
        n = n/4
        return self.isPowerOfFour(n)