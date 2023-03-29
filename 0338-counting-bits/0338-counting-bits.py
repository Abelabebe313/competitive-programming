class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        def recurtion(num):
            if num > n:
                return
            
            binar = bin(num)
            ans.append(binar.count('1'))
            recurtion(num+1)
            
        recurtion(0)
        return ans
        
        
        