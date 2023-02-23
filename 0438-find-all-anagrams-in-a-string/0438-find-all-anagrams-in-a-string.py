from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pdict = defaultdict(int)
        sdict = defaultdict(int)
        
        l = 0
        r = len(p)
        output = []
        if len(p) > len(s):
            return []
        else:
            for char in range(len(p)):
                pdict[p[char]] += 1
                sdict[s[char]] += 1

        while r <= len(s)-1:
            # print(sdict)
            if sdict == pdict:
                output.append(l)
                
            sdict[s[l]] -= 1
            if sdict[s[l]] == 0:
                del sdict[s[l]]
            sdict[s[r]] += 1
            r += 1
            l += 1
            
        if sdict == pdict:
            output.append(l)
        return output