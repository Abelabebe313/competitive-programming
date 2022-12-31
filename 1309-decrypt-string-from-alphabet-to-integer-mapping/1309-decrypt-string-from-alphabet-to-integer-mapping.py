class Solution:
    def freqAlphabets(self, s: str) -> str:
        ans = []
        n = len(s)-1
        
        while n >= 0:
            temp = []
            if s[n] == '#':
                temp = int(''.join(s[n-2:n]))
                ans.append(chr(96+temp))
                n -= 3
            else:
                ans.append(chr(96 + int(s[n]) ))
                n -= 1
        result = ''.join(reversed(ans))
        return result
    