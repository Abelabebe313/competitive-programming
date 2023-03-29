class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        for i in range(n+1):
            index = i
            while i:
                if i & 1:
                    ans[index] += 1
                    
                i >>= 1
                
        return ans
        
        
        