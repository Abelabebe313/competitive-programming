class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}

        def DFS(idx):
            if idx in dp:
                return dp[idx]
            if s[idx] == '0':
                return 0
            
            result = DFS(idx + 1)
            if ((idx+1)< len(s)) and (s[idx] == "1" or s[idx] == "2" and s[idx+1] in "0123456"):
                result += DFS(idx+2)
            
            dp[idx] = result
            return result
        return DFS(0)