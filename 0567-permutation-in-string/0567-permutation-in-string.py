from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        permi = s1[::-1]
        s2dict = defaultdict(int)
        permdict = defaultdict(int)
        
        l = 0
        r = len(s1)
        if len(s1) > len(s2):
            return False
        else:
            for i in range(len(s1)):
                s2dict[s2[i]] += 1
                permdict[permi[i]] += 1

        while r < len(s2):
            if permdict == s2dict:
                return True
            s2dict[s2[l]] -= 1
            if s2dict[s2[l]] == 0:
                del s2dict[s2[l]]
            s2dict[s2[r]] += 1
            l += 1
            r += 1
        if permdict == s2dict:
            return True
        
        return False
        
            
        
        