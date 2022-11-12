class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        numStr = str(num)
        divisor = ''
        count = 0
        for i in range(len(numStr)):
            divisor += numStr[i] 
            if i >= k:
                divisor = divisor[1:]
            if i >= k-1 and int(divisor):
                if num % int(divisor) == 0:
                    count += 1
        return count