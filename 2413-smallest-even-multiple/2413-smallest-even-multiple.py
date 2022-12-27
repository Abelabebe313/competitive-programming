class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        smallNum = 0
        if n % 2 == 0:
            smallNum = n
        else:
            smallNum = n * 2
        return smallNum