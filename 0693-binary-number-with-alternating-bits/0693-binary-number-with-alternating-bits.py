class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        
        num = n ^ (n >> 1)
        if num & (num + 1)==0:
            return True
        return False
        
        