class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(sqrt(c))
        while left <= right:
            if c == 0:
                return True
                break
            elif left**2 + right**2 > c:
                right -= 1
            elif left** 2 + right**2 < c:
                left += 1
            elif left**2+right**2 == c:
                return True
        return False