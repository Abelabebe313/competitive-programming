class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n+1)
        
        for i in range(1,n+1):
            if i % 2 == 0:
                idx = i//2
                ans[i] += ans[idx]
            else:
                idx = i//2
                ans[i] += (ans[idx]+1) 
                
        return ans
        
        