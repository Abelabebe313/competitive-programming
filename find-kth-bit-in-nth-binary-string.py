class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        def inverter(s):
            ans = []
            for i in s:
                if i == '1':
                    ans.append('0')
                else:
                    ans.append('1')
            return ans[::-1]

        def binaryString(n):
            if n == 1:
                return ["0"]
    
            ans = (binaryString(n-1) + ["1"] + inverter(binaryString(n-1)))
            return ans
        ans = binaryString(n)
        return ans[k-1]