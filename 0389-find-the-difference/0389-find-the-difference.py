class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = list(s)
        t = list(t)
        
        s.sort()
        t.sort()
        
        for i in range(len(s)):
            if s[i] != t[0]:
                return t[0]
            t.pop(0)
        return t[0]
            
            
        