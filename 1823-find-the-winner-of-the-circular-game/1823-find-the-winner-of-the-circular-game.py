class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        i = 0
        circle = [num + 1 for num in range(n)]
        while len(circle) != 1:
            i = (i + k - 1) % n
            circle.pop(i)
            n -= 1
            
        return circle[0]
        